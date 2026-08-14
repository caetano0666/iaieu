# IAieu eVc - favicon P1

Simbolo: circulo vermelho r10 em (16,12), filete 20x4 em (6,26). Grid 32x32.
Cores: vermelho #C1121F, preto #111111, fundo claro #F5F2EC.

## Regra de cor
Filete preto no fundo claro. Filete vermelho no fundo escuro.
Motivo: invertido em creme, o filete fica mais claro que o circulo e rouba a hierarquia da marca.
O favicon.svg faz essa troca sozinho por prefers-color-scheme.

## Arquivos
- favicon.svg          principal, troca de tema automatica
- favicon.ico          fallback (16, 32, 48). Usa filete vermelho, que le em qualquer fundo, porque ICO nao tem media query
- favicon-16/32/48/96.png       versao clara solta
- favicon-16/32/48/96-dark.png  versao escura solta
- apple-touch-icon.png 180, fundo creme e respiro, o iOS arredonda o canto
- icon-192.png, icon-512.png    PWA
- icon-512-maskable.png         PWA maskable, simbolo em 60% do quadro
- site.webmanifest
- head.html            as tags prontas

## Instalacao
Joga todos os arquivos na raiz do site e cola o conteudo de head.html dentro do <head>.
Depois de publicar, limpa o cache: navegador guarda favicon com teimosia.
