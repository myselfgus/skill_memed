https://doc.memed.com.br/docs/erros-comuns/blocked-frame-with-origin/

# Blocked a frame with origin

Se você está recebendo o erro `Uncaught DOMException: Blocked a frame with origin` ao carregar a sua página,
pode ser necessário ajustar o cabeçalho
`Referrer-Policy` da página que está carregando o módulo da Memed para o valor `strict-origin-when-cross-origin`.

Veja abaixo uma imagem desse erro:

![blocked-frame-with-origin.png](https://cdn.memed.com.br/doc/blocked-frame-with-origin.png)

### Como esse erro ocorre

Esse erro ocorre quando há uma tentativa de carregar recursos de uma página web com uma origem diferente da página principal que está sendo
carregada. Esse tipo de comportamento é conhecido como `cross-origin framing` e é uma medida de segurança implementada pelos navegadores para
prevenir que sites maliciosos carreguem conteúdo de outras páginas da web sem o consentimento do usuário.

Se o cabeçalho `Referrer-Policy` da sua aplicação estiver configurado como `same-origin`, o carregamento da Memed pode ser bloqueado. Isso ocorre
porque a Memed realiza uma verificação de domínio internamente através de um dos módulos que é carregado via iframe, e a presença do cabeçalho
`same-origin` pode impedir que essa verificação seja realizada corretamente.

Para obter mais informações sobre o cabeçalho Referrer-Policy, consulte a documentação
disponível em [Referrer-Policy](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Referrer-Policy).
