# Google Search Console: estado atual e rotina de uso

Este arquivo é para quem não é técnico. Cada passo diz onde clicar e o que você deve ver na tela.

O Google Search Console (vamos chamar de GSC) é o painel gratuito do Google que mostra se o site iaieu.com está aparecendo na busca, com quais palavras as pessoas chegaram e se alguma página está com problema.

Endereço para entrar: https://search.google.com/search-console
Entre com a conta Google czamma@gmail.com.

---

## 1. O que já está pronto (não precisa refazer)

| Item | Situação | Observação |
|---|---|---|
| Propriedade iaieu.com | Já verificada | Não precisa verificar de novo |
| Arquivo de verificação | `google7279386773b5d258.html` na raiz do site | NUNCA apague, NUNCA renomeie, NUNCA edite esse arquivo. Se ele sumir, o Google perde a verificação e o painel para de funcionar |
| Sitemap | Já enviado | Endereço: `https://iaieu.com/sitemap.xml` |
| robots.txt | Já publicado | Endereço: `https://iaieu.com/robots.txt` |

Resumo: a parte de instalação está concluída. O que resta é usar o painel de vez em quando. É isso que este arquivo ensina.

---

## 2. Como conferir se uma página nova foi indexada

"Indexada" quer dizer: o Google já leu a página e ela pode aparecer nos resultados de busca. Uma página que existe no site mas não está indexada é invisível para quem pesquisa.

Passo a passo:

1. Entre em https://search.google.com/search-console
2. No canto superior esquerdo tem uma caixinha com o nome da propriedade. Confirme que está escrito `iaieu.com`. Se estiver outro site, clique nessa caixinha e escolha `iaieu.com`.
3. Bem no topo da tela tem uma barra de pesquisa comprida com o texto cinza "Inspecionar qualquer URL em..." . Clique nela.
4. Cole o endereço completo da página, por exemplo: `https://iaieu.com/conteudos.html`
   Tem que ser o endereço completo, começando com `https://`. Não cole só `conteudos.html`.
5. Aperte Enter e espere. Aparece uma mensagem "Recuperando dados do índice do Google". Isso leva de 10 a 40 segundos. É normal.
6. Leia o resultado:

| O que aparece na tela | O que significa | O que fazer |
|---|---|---|
| "O URL está no Google" com um visto verde | Está tudo certo, a página está indexada | Nada |
| "O URL não está no Google" | O Google ainda não colocou a página no índice | Siga a seção 3 deste arquivo e peça a indexação |
| "O URL está no Google, mas tem problemas" | A página aparece na busca, mas alguma coisa secundária está errada, normalmente algo de dados estruturados ou de celular | Anote o texto exato do problema e mande para quem cuida do site |

Detalhe importante: página nova costuma demorar. Entre alguns dias e algumas semanas é normal. Não adianta pedir indexação todo dia.

---

## 3. Como pedir a indexação de uma URL

Use quando você publicou uma página nova, ou quando mudou bastante o texto de uma página que já existia, e quer avisar o Google.

1. Faça a inspeção da URL exatamente como na seção 2, passos 1 a 5.
2. Na tela de resultado, procure o botão escrito `SOLICITAR INDEXAÇÃO`. Ele fica logo abaixo do resultado, alinhado à direita.
3. Clique nele.
4. Aparece uma janelinha escrita "Testando se o URL pode ser indexado". Espere, leva cerca de um minuto.
5. Quando terminar, aparece uma confirmação verde: "Indexação solicitada. O URL foi adicionado a uma fila de rastreamento prioritário".
6. Clique em `OK` e pronto. Não faça de novo para a mesma página no mesmo dia, não acelera nada.

Limite do Google: mais ou menos 10 a 12 pedidos por dia por propriedade. Se aparecer "Você excedeu sua cota", espere até o dia seguinte.

Quando pedir indexação:
- Página nova publicada.
- Título ou descrição de uma página alterados.
- Texto principal reescrito.

Quando NÃO pedir:
- Trocou uma foto.
- Ajustou uma cor ou um espaçamento.
- Corrigiu uma vírgula.

---

## 4. Onde ver os termos de busca que trouxeram gente

1. No menu da esquerda, clique em `Desempenho`.
2. Vai abrir um gráfico e, embaixo dele, uma tabela.
3. No topo do gráfico existem quatro caixas: `Total de cliques`, `Total de impressões`, `CTR médio`, `Posição média`. Clique em cada uma para ligar ou desligar a linha correspondente no gráfico. Deixe pelo menos `Total de cliques` e `Total de impressões` ligadas.

O que cada número quer dizer, em português simples:

| Nome no painel | Significado |
|---|---|
| Impressões | Quantas vezes o site apareceu na lista de resultados do Google, mesmo que ninguém tenha clicado |
| Cliques | Quantas vezes alguém realmente clicou e entrou no site |
| CTR | A porcentagem de quem viu e clicou. Se apareceu 100 vezes e 3 clicaram, o CTR é 3% |
| Posição média | Em que lugar da lista o site apareceu, na média. 1 é o primeiro resultado. Quanto menor o número, melhor |

4. Logo abaixo do gráfico tem uma fileira de abas: `CONSULTAS`, `PÁGINAS`, `PAÍSES`, `DISPOSITIVOS`.
   - `CONSULTAS` é a mais útil: são as palavras que as pessoas digitaram no Google antes de chegar no site.
   - `PÁGINAS` mostra quais páginas do iaieu.com receberam esses cliques.
5. No canto superior esquerdo, acima do gráfico, tem um filtro de período escrito algo como `Últimos 3 meses`. Clique e escolha o período que quiser.
6. Para baixar a lista, clique em `EXPORTAR` no canto superior direito e escolha `Baixar CSV` ou `Google Planilhas`.

Como usar essa informação: se as pessoas estão chegando com uma pergunta que o site responde mal, vale escrever um conteúdo melhor sobre aquilo. As consultas são o retrato real do que o público procura, e valem mais do que qualquer palpite.

---

## 5. O que fazer quando aparece erro de cobertura

"Cobertura" é a parte do painel que lista páginas que o Google não conseguiu indexar.

1. No menu da esquerda, clique em `Indexação` e depois em `Páginas`.
2. A tela mostra dois blocos: páginas indexadas e páginas não indexadas.
3. Role para baixo até a tabela com o título "Por que as páginas não são indexadas".
4. Clique em cada linha para ver quais endereços estão naquele estado.

Tabela de tradução dos avisos mais comuns:

| Aviso do Google | O que está acontecendo | É problema? | Primeira coisa a fazer |
|---|---|---|---|
| Rastreada no momento, não indexada | O Google leu a página e decidiu não colocar no índice ainda | Normalmente não, é só espera | Aguarde algumas semanas. Se persistir, o texto da página provavelmente é curto ou parecido demais com outra página |
| Descoberta, não indexada no momento | O Google sabe que a página existe mas ainda não leu | Não | Aguarde. Pode pedir indexação uma vez |
| Página com redirecionamento | O endereço leva para outro endereço | Não, se foi de propósito | Confirme que o destino é a página certa |
| Erro do servidor (5xx) | O site não respondeu | Sim | Abra a página no navegador. Se abrir normal, foi uma falha momentânea. Se não abrir, avise quem cuida do site |
| Não encontrado (404) | O endereço não existe mais | Sim, se ele está no sitemap ou linkado no site | Ou republique a página, ou tire o link e tire a linha do `sitemap.xml` |
| Bloqueada pelo robots.txt | O arquivo robots.txt está proibindo o Google de ler | Sim | Confira `https://iaieu.com/robots.txt`. Ele deve dizer `Allow: /`. Se disser `Disallow: /`, está errado e precisa de correção urgente |
| Excluída pela tag noindex | A página tem um comando escondido mandando o Google ignorar | Sim, se não foi de propósito | Precisa de alguém técnico para remover a tag `noindex` do código da página |
| Página alternativa com tag canônica adequada | Duas páginas parecidas, o Google escolheu uma | Não | Nada a fazer |

Depois de corrigir alguma coisa, volte na linha do erro dentro de `Indexação > Páginas` e clique no botão `VALIDAR CORREÇÃO`. O Google vai reconferir sozinho e te avisar por e-mail em alguns dias.

Regra de bolso: aviso que aparece em 1 ou 2 páginas raramente é urgente. Aviso que aparece em todas as páginas de uma vez é urgente e pede socorro técnico.

---

## 6. Rotina mensal, lista de checagem

Reserve 15 minutos por mês. Sugestão: todo dia 1.

- [ ] Entrei no GSC e confirmei que a propriedade selecionada é `iaieu.com`.
- [ ] Abri `Desempenho`, coloquei o período em `Últimos 3 meses` e anotei: cliques, impressões, posição média.
- [ ] Na aba `CONSULTAS`, li as 20 primeiras linhas e anotei 3 termos novos que apareceram.
- [ ] Na aba `PÁGINAS`, conferi qual página teve mais cliques e qual teve zero.
- [ ] Abri `Indexação > Páginas` e comparei o número de páginas indexadas com o mês passado. Caiu? Investigar. Subiu ou ficou igual? Tudo bem.
- [ ] Conferi se apareceu algum erro novo na tabela "Por que as páginas não são indexadas".
- [ ] Se publiquei página nova no mês, inspecionei a URL dela e, se não estava indexada, pedi indexação.
- [ ] Abri `https://iaieu.com/google7279386773b5d258.html` no navegador e confirmei que o arquivo ainda carrega. Se der erro 404, a verificação está em risco.
- [ ] Abri `https://iaieu.com/sitemap.xml` e confirmei que a lista de páginas está completa e que as datas de `lastmod` correspondem à realidade.
- [ ] Anotei tudo no registro do mês.

Registro mensal, copie e preencha:

| Mês | Cliques | Impressões | Posição média | Páginas indexadas | Erros novos | Observação |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

---

## 7. Avisos importantes

- Ninguém pode garantir posição no Google. Nem agência, nem ferramenta, nem consultor. O que dá para fazer é remover obstáculos técnicos e publicar conteúdo que responde de verdade a uma pergunta real. O resultado vem do acúmulo, não de um botão.
- Número no GSC oscila. Uma queda de uma semana não quer dizer nada. Compare mês contra mês, nunca dia contra dia.
- O GSC mostra apenas o Google. Bing e Copilot ficam em outro painel, veja `BING-WEBMASTER-SETUP.md`.
