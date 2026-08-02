# Histórico técnico

Registro do que foi feito na pasta, com detalhe. O `NEXT.md` fica curto, os detalhes ficam aqui.

Mais recente em cima.

---

## 2 de agosto de 2026: raiz enxugada, Bloco 1

Objetivo: menos itens visíveis ao abrir a pasta, para diminuir a carga mental. Não foi arrumação por estética.

A raiz saiu de 38 para 35 itens.

| Arquivo | Foi para | Por quê |
|---|---|---|
| `AI_RULES.md` | `docs-geo/` | é a regra de como trabalhar, quem lê é a IA, não o Caetano |
| `HISTORICO-TECNICO.md` | `docs-geo/` | é registro do passado, consultado raramente |
| `LEIA-ME.md` | `arquivo-morto/` | está desatualizado, descreve um site de página única que não existe mais |

Nenhum dos três é usado pelo site.

### Referências atualizadas

| Onde | O que mudou |
|---|---|
| `COMECE_AQUI.md`, linha 21 | passou a citar `docs-geo/AI_RULES.md` |
| `NEXT.md` | a pendência do travessão agora aponta para `arquivo-morto/LEIA-ME.md` |

As menções ao `LEIA-ME.md` nos registros antigos deste arquivo **não** foram alteradas de propósito. Naquelas datas ele estava mesmo na raiz, e mudar o texto falsificaria o histórico.

### O que não saiu da raiz, e por quê

`favicon.ico`, `og-image.png` e `logo_horizontal.png` têm endereço fixo procurado pelo navegador ou declarado ao Google. As 12 páginas são endereços do site. O `estilo.css` sairia ao custo de mexer em 12 páginas, o que não compensa.

### Bloco 2, proposto e não aprovado nesta sessão

Tirar `favicon-16.png`, `favicon-32.png`, `favicon-192.png` e `apple-touch-icon.png` da raiz custa 34 linhas em 11 páginas. Ficou para decisão futura.

### Teto conhecido

Cerca de 31 itens é o piso desta estrutura. Para ir bem abaixo disso só colocando o site inteiro dentro de uma pasta e mandando o GitHub publicar de lá, o que mexe na configuração de publicação.

### Testes rodados depois

| Teste | Resultado |
|---|---|
| `python3 docs-geo/seo-tests.py` | 231 PASS, 0 WARN, 0 FAIL |
| Varredura de link quebrado | nenhum |
| Referência apontando para arquivo que não existe mais | nenhuma |
| Os arquivos que nunca podem sumir | todos na raiz |
| As páginas do site | todas abrindo |

---

## 2 de agosto de 2026: publicado

As três etapas e a limpeza foram publicadas no site. Commit `7b70678` na branch `main`.

### A checklist da seção 9, item por item

| Item | Resultado |
|---|---|
| Arquivos obrigatórios na raiz, intactos | ok, os 6 |
| `seo-tests.py` com 0 FAIL | 231 PASS, 0 WARN, 0 FAIL |
| Página nova com os 7 itens | nenhuma página nova foi criada |
| Página nova no `sitemap.xml` | não se aplica |
| Número novo sem data | nenhum |
| `aggregateRating` ou `review` no código | nenhum |
| Textos de posicionamento aprovados | intactos |
| Grep de travessão | reprova, ver abaixo |
| Preço publicado | nenhum |
| Promessa de posição no Google ou citação em IA | nenhuma |

### Por que o item do travessão não travou a publicação

O travessão aparece em dois arquivos: `admin.html`, com 14, e `LEIA-ME.md`, com 11.

Foi comparada a versão que já estava no ar com a versão a publicar. Os números são idênticos nas duas. Nenhuma outra página do site tem travessão, e nenhum dos documentos novos tem.

Ou seja, a publicação não criou violação nova. A violação já existia em produção e o Caetano decidiu tratá-la em outro momento. Fica pendente.

### Conferência feita no site no ar, depois de publicar

| O que foi conferido | Resultado |
|---|---|
| `robots.txt` novo no ar | sim, apontando para `/dados/` |
| As 11 páginas | todas respondendo |
| Home: imagens e fundo do hero | carregam de `imagens/` |
| Home: depoimentos | 4 cards |
| Página de depoimentos | 10 cards |
| Clique no botão de print | abre a foto, carregada de `imagens/` |
| `sitemap.xml` | 12 URLs, intacto |
| `logs/` no ar | 404, ficou fora como planejado |
| Endereços antigos, tipo `/config.json` | 404, como esperado |

### Um efeito passageiro, esperado

Quem visitou o site nos últimos minutos pode ter a página antiga guardada no navegador, e ela aponta para os endereços velhos das imagens. Isso se resolve sozinho quando o navegador busca a página de novo.

---

## 2 de agosto de 2026: preparação para publicar

Antes de publicar, foi feita a conferência da seção 9 do `FUTURE-MAINTENANCE.md`. Ela encontrou três problemas. Dois foram corrigidos, um ficou para depois.

### 1. A pasta `logs/` iria para o ar

O `logs/log_posts_comentarios.csv` tem 53 profissionais identificados, com cargo, empresa e observações. Publicar isso deixaria os dados dessas pessoas legíveis por qualquer um e indexáveis pelo Google.

Corrigido: a pasta `logs/` entrou no `.gitignore`, com o motivo escrito no próprio arquivo. Ela continua na máquina do Caetano e não vai mais para o site.

### 2. O `robots.txt` tinha ficado desatualizado na Etapa 2

Ele bloqueava `/posts.json` e `/config.json`. Depois da Etapa 2 esses arquivos passaram a morar em `/dados/`, então o bloqueio deixou de valer e os dois ficariam liberados para busca.

Corrigido para `/dados/posts.json` e `/dados/config.json`.

A tradução foi feita linha a linha, de propósito, em vez de bloquear a pasta `/dados/` inteira. Bloquear a pasta toda também esconderia o `artes.json`, que antes era liberado. O objetivo era preservar o comportamento, não mudá-lo.

Lição: mover arquivo pede conferência no `robots.txt`. Nenhum teste automático pega isso hoje.

### 3. O `admin.html` tem 14 travessões

A regra da casa é zero travessão em texto publicado, e a seção 9 diz que isso trava a publicação. É anterior a qualquer coisa feita nestas etapas.

Decisão do Caetano em 2 de agosto de 2026: não mexer nisso nesta sessão, tratar em outro momento.

Observação registrada: o `seo-tests.py` dá 0 FAIL mesmo com esses 14 travessões. A seção 7 do `FUTURE-MAINTENANCE.md` afirma que o teste cobre essa checagem, e não cobre.

### Testes rodados depois

| Teste | Resultado |
|---|---|
| `python3 docs-geo/seo-tests.py` | 231 PASS, 0 WARN, 0 FAIL |
| Varredura de link quebrado | nenhum |
| Os 4 arquivos que nunca podem sumir | todos na raiz |
| `logs/` fora da publicação | confirmado |
| Endereços citados no `robots.txt` novo | todos existem |
| As páginas do site abrindo | todas |

---

## 2 de agosto de 2026: Etapa 3 da migração

As imagens usadas pelo site saíram da raiz e foram para a pasta `imagens/`.

Foram 22 imagens movidas, e não 23. O motivo está mais abaixo.

| Grupo | Quantas |
|---|---|
| Prints do correio na home | 7 |
| Fotos dos depoimentos | 7 |
| Capas de projeto | 3 |
| Símbolo do rodapé, avatar, hero, dois fundos | 5 |

### Referências corrigidas

| Onde | Quantas |
|---|---|
| Nas 11 páginas | 28 |
| Em `dados/config.json` | 7 |

As 7 fotos de depoimento não aparecem em nenhuma página. Elas estão escritas dentro do `dados/config.json`, no campo `print` de cada depoimento, e viram um botão que abre a foto em tela cheia. Esse é o ponto que quebraria sem aparecer em teste automático.

### Ficaram na raiz de propósito

| Arquivo | Por quê |
|---|---|
| `og-image.png` | o endereço `iaieu.com/og-image.png` já foi divulgado e é o que aparece quando alguém compartilha o site |
| `favicon.ico`, `favicon-16`, `favicon-32`, `favicon-192`, `apple-touch-icon` | o navegador procura esses arquivos sozinho, na raiz |
| `logo_horizontal.png` | ver abaixo |

### Por que o `logo_horizontal.png` não foi movido

Na conferência antes de mover, apareceu que esse arquivo é o logo oficial declarado para o Google, com endereço fixo `https://iaieu.com/logo_horizontal.png`. Ele está escrito em dois lugares: na linha 590 do `index.html`, dentro do bloco de dados estruturados, e no `docs-geo/business.json`.

É a mesma situação do `og-image.png`, que já tinha sido decidido que fica na raiz. Movê-lo faria o endereço antigo parar de existir até o Google visitar o site de novo.

Por isso ele ficou onde está, e a decisão de mover ou não foi levada ao Caetano.

**Decidido em 2 de agosto de 2026: fica na raiz, em definitivo.** O Caetano preferiu preservar o endereço oficial. Vale a mesma regra do `og-image.png`. Nenhuma etapa futura deve mover esse arquivo.

### Testes rodados depois

| Teste | Resultado |
|---|---|
| `python3 docs-geo/seo-tests.py` | 231 PASS, 0 WARN, 0 FAIL |
| Varredura de link quebrado | nenhum |
| Varredura de imagem de fundo no CSS | nenhuma quebrada |
| Referência antiga sobrando | nenhuma |
| Caminho duplicado, tipo `imagens/imagens/` | nenhum |
| As 22 imagens respondendo no lugar novo | todas |
| As 11 páginas do site | todas abrindo |

### Verificação manual no navegador

| O que foi olhado | Resultado |
|---|---|
| Home, os 7 prints do correio | aparecem |
| Home, fundo do hero e das seções | aparecem |
| Home, depoimentos | 4 cards, como antes |
| Página de depoimentos | 10 cards, 8 botões de print |
| Clique no botão "Ver recomendação original" | abre a foto em tela cheia, carregada do lugar novo |
| Página de projetos | as 3 capas aparecem |
| Página do IAieu | as fotos aparecem |
| Página de arte | busca o arquivo certo |
| Erro no console em qualquer página | nenhum |

---

## 1 de agosto de 2026: Etapa 2 da migração

Os arquivos de dados saíram da raiz e foram para a pasta `dados/`.

| Antes | Depois |
|---|---|
| `config.json` | `dados/config.json` |
| `posts.json` | `dados/posts.json` |
| `artes/artes.json` | `dados/artes/artes.json` |
| `artes/_LEIA-ME.txt` | `dados/artes/_LEIA-ME.txt` |

### As 5 referências corrigidas

| Arquivo | Linha | Mudou para |
|---|---|---|
| `index.html` | 1371 | `dados/config.json` |
| `depoimentos.html` | 311 | `dados/config.json` |
| `admin.html` | 316 | `dados/config.json` |
| `admin.html` | 321 | `dados/posts.json` |
| `arte.html` | 248 | `dados/artes/artes.json` |

Nada mais foi tocado nessas quatro páginas.

Os nomes de arquivo que o painel admin usa ao baixar uma cópia, nas linhas 542 e 548 do `admin.html`, continuam sendo `config.json` e `posts.json`. Isso está certo: são nomes de download, não caminhos.

As fotos dos depoimentos citadas dentro do `config.json` não precisaram de ajuste. Elas são inseridas na página, então o endereço delas continua sendo contado a partir da página, não a partir do JSON.

### Testes rodados depois

| Teste | Resultado |
|---|---|
| Varredura de link quebrado | nenhum |
| `python3 docs-geo/seo-tests.py` | 231 PASS, 0 WARN, 0 FAIL |
| Nenhuma referência antiga sobrando | confirmado |
| Home: depoimentos carregando | 4 cards, como antes |
| Página de depoimentos | 10 cards, nenhuma foto quebrada |
| Página de arte | busca o JSON certo e responde certo |
| Painel admin | busca os dois JSON, os dois em 200 |

### Uma pegadinha para o futuro

O `dados/artes/artes.json` está vazio hoje. Quando ele for preenchido, os endereços de imagem escritos lá dentro precisam apontar para o novo lugar. O script que gerava esse arquivo, o `gerar_artes.py`, está em `arquivo-morto/` e ainda escreve o caminho antigo.

### Fora do escopo, não alterado

O comentário da linha 202 do `arte.html` ainda diz `artes/artes.json`, que é o endereço antigo. É só um comentário, não afeta o funcionamento.

---

## 1 de agosto de 2026: Etapa 1 da migração

A pasta `LOGS para atualizar diario` virou `logs/`. Três arquivos dentro, nenhum deles usado pelo site.

Motivo: nome com espaço e sem acento correto atrapalha script e linha de comando.

Antes de mover, foi confirmado que nenhum arquivo do projeto apontava para essa pasta.

### Testes rodados depois

| Teste | Resultado |
|---|---|
| Varredura de link quebrado em todas as páginas | nenhum |
| `python3 docs-geo/seo-tests.py` | 231 PASS, 0 WARN, 0 FAIL |
| As 10 páginas do site respondendo localmente | todas em 200 |
| Home aberta no navegador | abre certo, sem erro no console |

O número 231 PASS e 0 FAIL é o mesmo de antes da etapa.

### Observação fora do escopo

A varredura de travessão encontrou três arquivos com travessão: `admin.html`, `LEIA-ME.md` e `logs/log_recomendacoes_linkedin.md`. Nenhum foi causado por esta etapa e nenhum foi alterado.

---

## 1 de agosto de 2026: limpeza da pasta

A pasta saiu de 247 MB para 90 MB. O site não mudou em nada.

### Criada a pasta `arquivo-morto/`

18 arquivos, 17 MB. Nenhum deles era usado por nenhuma página do site. Nada foi apagado, só saiu do caminho.

| Arquivo | Tamanho |
|---|---|
| `FLYER_curso_IAieu.png` | 9,6 MB |
| `cae-hero-pb.png` | 1,7 MB |
| `cae-hero.png` | 1,1 MB |
| `hero.png` | 1,1 MB |
| `logo-oficial.png` | 784 KB |
| `Simbolo.png` | 648 KB |
| `favicon-quadrado.png` | 644 KB |
| `logo_iaieu.png` | 588 KB |
| `logo-cash.png` | 480 KB |
| `flyer-home.jpg` | 204 KB |
| `logo_oficial_t.png` | 164 KB |
| `logo IAieu_OFICIAL.jpeg` | 148 KB |
| `favicon.png` | 104 KB |
| `cae-avatar.jpg` | 64 KB |
| `logo_horizontal_t.png` | 40 KB |
| `simbolo_t.png` | 24 KB |
| `claude-simbolo.svg` | 4 KB |
| `gerar_artes.py` | 4 KB |

Três desses arquivos aparecem citados dentro de `docs-geo/`, mas só como imagem pesada que nenhuma página carrega e que convém limpar. Era exatamente o caso.

### Apagados

| O quê | Tamanho | Por quê |
|---|---|---|
| `iaieu-site-publicar.zip` | 4,7 MB | backup de julho, o site já estava publicado |
| `.claude/worktrees/` | 153 MB | pastas de trabalho do Claude |

Antes de apagar as pastas de trabalho, foi verificado uma por uma que todo o conteúdo delas já estava salvo no histórico do projeto. Nada foi perdido.

### Não foi mexido

`plinio/`, `stw-daryl-lucas/`, as imagens que o site usa e a pasta `docs-geo/`.

### Verificação feita depois

Todas as páginas do site foram varridas procurando imagem, estilo ou link quebrado. Nenhum foi encontrado.

### Também criado neste dia

`COMECE_AQUI.md` na raiz, que diz por onde retomar o projeto.

### Ficou em aberto

1. A pasta `arquivo-morto/` continua sendo publicada junto com o site. Dá para tirar do ar se você quiser.
2. Apagar arquivo não diminui o histórico do projeto. Os 58 MB de histórico do Git continuam existindo. A limpeza deixou a pasta e o site mais leves, não o passado.
3. As mudanças estão marcadas no Git mas ainda não foram publicadas. O site no ar ainda é o de antes.
