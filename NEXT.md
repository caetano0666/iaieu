# NEXT

## Missão

Construir um sistema de trabalho com IA que funcione mesmo quando eu esquecer onde parei.

## Onde parei

**A V2 está no ar. Publicada, validada em produção e oficialmente encerrada em 04/08/2026.**

Em 4 de agosto de 2026 o site inteiro passou por uma evolução de direção de arte, em quatro rodadas no mesmo dia: a home, o refino da home, as nove páginas internas, e a auditoria final antes de publicar.

Nenhuma palavra de conteúdo foi alterada em nenhuma das rodadas. Só ritmo, escala, cor, ordem de seção, espaçamento, borda, raio e comportamento.

O que mudou, em resumo:

1. A prova subiu para o começo da home. Casos e Caso 01 aparecem logo depois do hero.
2. Entraram áreas claras no off-white da marca, sempre no bloco de prova. Duas na home, uma em cada interna.
3. O gradiente roxo e azul virou raro. Existe na marca, nos botões e na pergunta dos trinta dias. Nos títulos, a ênfase virou monocromática.
4. O título do hero cresceu de 50px para 78px.
5. A pergunta dos trinta dias ganhou uma tela quase vazia só dela.
6. Saíram as duas imagens de banco, as partículas em rede e o planeta com halo roxo, e a rosa dos ventos da página de conteúdos. No lugar entrou uma malha fina em CSS.
7. O botão do WhatsApp ficou silencioso e só acende no hover.
8. O menu passou a mostrar Casos e Depoimentos.
9. Corpo de texto saiu do peso 300 para 400.
10. O âmbar foi removido do site inteiro, inclusive o uso antigo, anterior a esta evolução. A paleta agora é só preto, off-white, roxo e azul.
11. O bloco `.analogia-box` da `sobre.html`, que usava classes sem CSS e ficava sem formatação no ar, foi resolvido: a definição saiu do CSS interno da página do método e passou para o `estilo.css`, então vale para as duas páginas e o problema não volta.
12. A página Arte saiu do percurso do visitante, última correção antes da publicação.

Onde o sistema mora: o CSS novo da home está num bloco único no fim do `<style>` do `index.html`, marcado como "EVOLUCAO DA DIRECAO DE ARTE". O das internas está no fim do `estilo.css`, que as nove dividem. Nenhum arquivo novo foi criado, de propósito, porque o `.gitignore` bloqueia tudo por padrão. Apagar esses dois blocos devolve o visual anterior.

## A decisão sobre a página Arte, em 04/08/2026

A `arte.html` estava publicada, estava no `sitemap.xml` e recebia um link da página Projetos com a chamada "Veja também as minhas artes". A galeria lê de `dados/artes/artes.json`, que está com a lista vazia, então a página entregava "Em breve, novas artes por aqui".

Decisão do proprietário: **não mostramos aquilo que ainda não entregamos.** A página saiu do percurso do visitante e continua no repositório para uso futuro.

O que foi feito: o link foi removido da `projetos.html`, junto com a seção que só existia para ele. A URL saiu do `sitemap.xml`. A linha saiu do `llms.txt`. A página ganhou `noindex` para não aparecer na busca enquanto estiver vazia. E ela saiu da lista `PAGINAS` do `docs-geo/seo-tests.py`, de forma consciente e documentada num comentário dentro do próprio arquivo, mas continua sendo checada pelas regras da casa, então ela nunca fica com travessão.

**Para devolver a página ao ar quando a galeria estiver pronta:** preencher `dados/artes/artes.json`, devolver a linha `"arte.html"` ao dicionário `PAGINAS` do `seo-tests.py`, devolver o bloco `<url>` ao `sitemap.xml` com a data real, tirar o `noindex`, igualar o menu ao das outras páginas e refazer o link na `projetos.html`.

## Estado dos testes

`python3 docs-geo/seo-tests.py` fecha em **232 PASS, 0 WARN, 0 FAIL**. O número de testes caiu de 247 para 232 porque a `arte.html` deixou de ser uma das páginas públicas conferidas.

Também foram conferidos, fora da bateria: contraste de cada texto contra o fundo real em que ele cai, em dez páginas, zero falha; estouro de layout e imagem quebrada em desktop e celular, nenhum; link interno quebrado, nenhum; e comparação do mesmo componente entre as dez páginas, com as nove internas batendo cem por cento entre si.

## Publicação e validação em produção, 04/08/2026

Commits `0c0a599` e `ce6913c` confirmados no GitHub. O site foi validado no ar, em desktop e em celular.

O que foi conferido e está íntegro: as dez páginas públicas respondendo 200, um H1 por página, menu com os mesmos cinco itens em todas, áreas claras no lugar, rodapé e botão do WhatsApp em todas, 23 alvos internos entre páginas, imagens e CSS sem um link quebrado, `sitemap.xml` com 12 URLs e sem a Arte, `robots.txt` intacto, `llms.txt` sem a Arte, zero âmbar, zero travessão, botões todos em pílula, e um único texto com gradiente na home inteira, que é a pergunta dos trinta dias. O bloco da `sobre.html` que estava sem formatação apareceu no ar com caixa, borda e espaçamento.

Nenhuma correção foi necessária depois da publicação.

## Uma nota operacional que não é defeito do site

Durante a validação, o navegador insistia em mostrar a versão antiga mesmo com o site novo no servidor. A causa era um Service Worker fantasma: uma versão antiga do site registrou um `sw.js` no navegador, e esse registro continuou vivo guardando páginas em cache. O arquivo `sw.js` não existe mais no projeto, e o endereço `https://iaieu.com/sw.js` responde 404.

Consequência prática: quem visitou o site em julho pode ver a versão antiga por algum tempo. Isso se resolve sozinho, porque o navegador desregistra o Service Worker quando tenta atualizá-lo e recebe 404. Não há nada a corrigir no projeto.

Se acontecer com você, abra o site numa janela anônima para ver a versão real.

## Daqui para frente

O site deixou de ser projeto em desenvolvimento e passou a ser produto em operação. Melhoria só nasce de resultado real de uso, nunca de refinamento de direção de arte por iniciativa própria:

- O que o Analytics mostrar sobre onde as pessoas param de rolar e por onde saem.
- Dúvida que se repetir na conversa de WhatsApp, porque dúvida repetida é buraco de página.
- A página Conteúdos, quando existirem mais textos publicados.
- A página Arte, quando a galeria existir. O passo a passo para devolvê-la está registrado acima.

## Próxima ação

Nenhuma. A V2 está encerrada.
