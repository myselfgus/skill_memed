# skill_memed

Skill para Claude que ensina a integrar a **prescrição digital Memed** em sistemas de saúde, gerada a partir da documentação oficial em <https://doc.memed.com.br/docs/intro/>.

## Conteúdo

```
memed-prescricao/
├── SKILL.md                  # fluxo essencial, regras de homologação, diagnóstico e índice
├── references/               # documentação oficial convertida para Markdown, por tema
│   ├── boas-praticas.md
│   ├── visao-geral.md
│   ├── backend.md
│   ├── backend-tabelas.md    # cidades e especialidades (IDs)
│   ├── frontend.md
│   ├── comandos-mdhub.md
│   ├── eventos-mdhub.md
│   ├── como-fazer.md
│   ├── erros-comuns.md
│   ├── duvidas-frequentes.md
│   └── assinaturas-digitais.md
├── scripts/atualizar_docs.py # baixa a doc de novo e regenera references/
└── evals/evals.json          # casos de teste usados para validar a skill
```

## Instalação

Copie a pasta `memed-prescricao/` para `~/.claude/skills/` (Claude Code) ou importe o arquivo `memed-prescricao.skill` em claude.ai → Configurações → Skills.

## Atualizar a documentação

```bash
pip install beautifulsoup4   # e tenha o pandoc instalado
python3 memed-prescricao/scripts/atualizar_docs.py
```
