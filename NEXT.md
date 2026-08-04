# NEXT

## Missão

Construir um sistema de trabalho com IA que funcione mesmo quando eu esquecer onde parei.

## Onde parei

**A V2 do site está encerrada e aprovada. Falta só o push.**

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

## Próxima ação

**Publicar.** Rodar `python3 docs-geo/seo-tests.py` para conferir os 0 FAIL, e dar `git push`. O commit da V2 já está feito.

Depois de publicado, abrir o site no celular e conferir página por página, que é onde chega a maior parte de quem visita.
