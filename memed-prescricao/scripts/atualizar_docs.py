#!/usr/bin/env python3
"""Baixa a documentação pública da Memed e regenera references/*.md.

Uso:
    python3 scripts/atualizar_docs.py [--base https://doc.memed.com.br] [--cache DIR]

Requisitos: beautifulsoup4 (pip install beautifulsoup4) e pandoc no PATH.

O sitemap da Memed lista URLs em docs.memed.com.br, mas o conteúdo também é
servido em doc.memed.com.br; o host de --base é usado para todas as páginas.
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date

from bs4 import BeautifulSoup

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF_DIR = os.path.join(SKILL_DIR, "references")

# (arquivo de saída, título, função que decide se o slug pertence à seção)
SECTIONS = [
    ("boas-praticas.md", "Boas práticas de integração e critérios de homologação",
     lambda s: s == "boas-praticas-integracao"),
    ("visao-geral.md", "Visão geral, primeiros passos, carregamento, exibição e credenciais",
     lambda s: s in ("intro", "primeiros-passos", "modos-de-carregamento",
                     "modos-de-exibicao", "obter-credenciais", "integracao-tasy-mv")),
    ("backend.md", "Backend / API REST da Memed",
     lambda s: (s == "backend-api" or s.startswith("backend/"))
     and s not in ("backend/cidades", "backend/especialidades")),
    ("backend-tabelas.md", "Tabelas de referência: cidades e especialidades",
     lambda s: s in ("backend/cidades", "backend/especialidades")),
    ("frontend.md", "Frontend: script, autenticação, MdSinapsePrescricao/MdHub, estilo",
     lambda s: s.startswith("frontend") and "comandos-mdhub" not in s
     and "eventos-mdhub" not in s),
    ("comandos-mdhub.md", "Comandos MdHub (MdHub.command.send)",
     lambda s: "comandos-mdhub" in s),
    ("eventos-mdhub.md", "Eventos MdHub (MdHub.event.add)",
     lambda s: "eventos-mdhub" in s),
    ("como-fazer.md", "Como fazer (tutoriais)", lambda s: s.startswith("como-fazer")),
    ("erros-comuns.md", "Erros comuns e soluções", lambda s: s.startswith("erros-comuns")),
    ("duvidas-frequentes.md", "Dúvidas frequentes", lambda s: s.startswith("duvidas-frequentes")),
    ("assinaturas-digitais.md", "Assinaturas digitais (certificados em nuvem)",
     lambda s: s.startswith("assinaturas-digitais")),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "memed-skill-updater"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8")


def cell(c):
    return re.sub(r"\s+", " ", c.get_text(" ", strip=True)).replace("|", "\\|")


def table_md(tb):
    rows = [[cell(c) for c in tr.find_all(["th", "td"])] for tr in tb.find_all("tr")]
    rows = [r for r in rows if r]
    if not rows:
        return ""
    n = max(len(r) for r in rows)
    rows = [r + [""] * (n - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * n]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def html_to_md(html, base):
    soup = BeautifulSoup(html, "html.parser")
    art = soup.find("article") or soup.find("main")
    if art is None:
        return ""
    for t in art.select("nav, .pagination-nav, .theme-doc-footer, .hash-link, button, "
                        ".theme-doc-toc-mobile, svg, .theme-doc-breadcrumbs"):
        t.decompose()
    tables = {}
    for i, tb in enumerate(art.find_all("table")):
        key = f"TABLEPH{i}X"
        tables[key] = table_md(tb)
        p = soup.new_tag("p")
        p.string = key
        tb.replace_with(p)
    for h in art.select("[class*=admonitionHeading]"):
        h.string = "**" + h.get_text(" ", strip=True) + "**"
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=str(art), capture_output=True, text=True, check=True).stdout
    for k, v in tables.items():
        md = md.replace(k, "\n" + v + "\n")
    md = md.replace("``` prism-code", "```")
    md = md.replace("\\*\\*", "**")
    md = re.sub(r"!\[\]\(data:image[^)]*\)", "", md)
    # cartões de índice do Docusaurus ("📄️ Título" + resumo) não trazem conteúdo
    md = re.sub(r"\[\]\([^)]*\)\n+## 📄️ [^\n]*\n+[^\n]*\n?", "", md)
    md = re.sub(r"\]\(/docs/", f"]({base}/docs/", md)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def demote(md):
    # cada página vira uma seção de nível 2 dentro do arquivo de referência
    return re.sub(r"^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", md, flags=re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="https://doc.memed.com.br")
    ap.add_argument("--cache", help="diretório com HTML já baixado (<slug com __>.html)")
    args = ap.parse_args()
    base = args.base.rstrip("/")

    sitemap = fetch(base + "/sitemap.xml")
    slugs = []
    for loc in re.findall(r"<loc>([^<]+)</loc>", sitemap):
        m = re.search(r"/docs/(.+?)/?$", loc)
        if m:
            slugs.append(m.group(1))

    pages = {}
    for slug in slugs:
        cached = args.cache and os.path.join(args.cache, slug.replace("/", "__") + ".html")
        if cached and os.path.exists(cached):
            html = open(cached, encoding="utf-8").read()
        else:
            try:
                html = fetch(f"{base}/docs/{slug}/")
            except Exception as e:  # noqa: BLE001
                print(f"falhou {slug}: {e}", file=sys.stderr)
                continue
        md = html_to_md(html, base)
        if md and len(re.sub(r"^#.*$", "", md, flags=re.M).strip()) > 0:
            pages[slug] = md

    os.makedirs(REF_DIR, exist_ok=True)
    used = set()
    for fname, title, match in SECTIONS:
        sel = [s for s in slugs if s in pages and match(s) and s not in used]
        used.update(sel)
        if not sel:
            continue
        toc = "\n".join(f"- {pages[s].splitlines()[0].lstrip('# ').strip()} — "
                        f"`{base}/docs/{s}`" for s in sel)
        body = "\n\n---\n\n".join(
            f"<!-- fonte: {base}/docs/{s} -->\n" + demote(pages[s]) for s in sel)
        with open(os.path.join(REF_DIR, fname), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\nExtraído de {base}/docs em {date.today().isoformat()}.\n\n"
                    f"## Páginas neste arquivo\n\n{toc}\n\n---\n\n{body}\n")
        print(f"{fname}: {len(sel)} páginas")
    left = [s for s in pages if s not in used]
    if left:
        print("páginas sem seção:", left, file=sys.stderr)


if __name__ == "__main__":
    main()
