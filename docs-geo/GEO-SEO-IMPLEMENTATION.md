# O que foi implementado

Rodada de 30 de julho de 2026, partindo do commit `073d1c8` que estava em produção.

Regra que guiou tudo: **nenhum texto de posicionamento aprovado foi reescrito.** Todo conteúdo novo é adição. A verificação automática de integridade de texto confirmou 42 trechos adicionados e nenhuma frase aprovada alterada. As duas únicas trocas em texto existente foram travessões no subsite da Sparta Team Wear, que violavam a regra da casa.

## Correção mais urgente

**A imagem de compartilhamento da home estava quebrada.** O `og:image` apontava para `https://iaieu.com/site4.png`, arquivo que virou `.webp` na otimização de imagens e passou a retornar 404. Todo link do iaieu.com compartilhado no WhatsApp, LinkedIn ou Instagram aparecia sem imagem. Agora aponta para `og-image.png`, que existe e tem as dimensões corretas de 1200x630. O teste automático passou a verificar se o arquivo apontado existe de verdade, para isso não voltar a acontecer.

## Metadata, nas nove páginas

| O que | Antes | Agora |
|---|---|---|
| `canonical` | nenhuma página tinha | todas, autorreferente |
| `og:site_name` | ausente | `IAieu` |
| `og:locale` | ausente | `pt_BR` |
| `og:image` | uma quebrada, subsites sem nenhuma | absoluta em todas, com dimensões e texto alternativo |
| `twitter:title`, `description`, `image` | ausentes | presentes |
| `robots` | ausente | `index, follow, max-image-preview:large, max-snippet:-1` |
| description do subsite STW | não existia | escrita |

O `max-image-preview:large` importa para os resumos gerados por IA: sem ele, a prévia de imagem do site fica limitada a miniatura.

## Dados estruturados, de zero a 25 entidades

O site não tinha um único bloco de JSON-LD. Agora cada página tem um `@graph` com identificadores estáveis. O detalhe do inventário está em `SCHEMA-INVENTORY.md` e a lógica das entidades em `ENTITY-MAP.md`.

A decisão central: **Organization e Person separadas**, ligadas por `founder` e `worksFor`. Quem pergunta a um assistente "quem me ajuda com IA no meu negócio" busca uma pessoa; quem pergunta "o que é o IAieu" busca a marca. Entidades separadas respondem bem às duas perguntas.

Os três serviços viraram entidades `Service` com `Offer` **sem preço**, o que é válido em Schema.org e honesto. Os dois subsites viraram `CreativeWork` com o IAieu como criador.

## Conteúdo novo e visível

Duas seções foram adicionadas na home. Ambas são texto visível, não schema escondido.

**"O que é o IAieu"**, logo depois do hero: responde em quatro parágrafos o que é, para quem é, o que a pessoa recebe e como falar com você. Existe porque assistentes de IA citam a resposta que encontram nas primeiras linhas, e porque um visitante que caiu na página por acaso precisa entender o negócio em quinze segundos.

**"Perguntas frequentes"**, antes do CTA final: sete perguntas reais de cliente, incluindo "quanto custa" (respondida apontando para a conversa, sem valor) e "o que o IAieu não faz". Cada pergunta e resposta está espelhada palavra por palavra no `FAQPage` do schema, e existe um teste automático que falha se alguma pergunta existir só no schema.

## Infraestrutura

| Arquivo | O que mudou |
|---|---|
| `robots.txt` | Onze bots de IA declarados explicitamente (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Perplexity-User, Google-Extended, Applebot, CCBot). Bloqueio de `admin.html`, `docs-geo/`, `posts.json` e `config.json`. |
| `sitemap.xml` | Nove URLs, agora incluindo os dois subsites de portfólio. `lastmod` real, que estava congelado em 25 de julho. |
| `llms.txt` | Novo. Resumo do site em texto simples, com aviso de que o formato é experimental e que o Google não o usa. Instrui como citar o IAieu e proíbe atribuir preço ou prazo. |
| chave IndexNow | Nova, hospedada na raiz. Ping documentado em `BING-WEBMASTER-SETUP.md`. |
| `404.html` | Novo. Antes o GitHub Pages entregava a página genérica dele, fora da identidade do site. |
| `admin.html` | Ganhou `noindex, nofollow`. Estava respondendo 200 em produção sem estar linkado em lugar nenhum: um painel interno exposto ao rastreamento. |

## Acessibilidade e estrutura

O subsite da Sparta Team Wear tinha **dois H1**. O segundo virou H2, com o texto idêntico: só a etiqueta mudou. Agora todas as nove páginas têm exatamente um H1.

## Analytics

O contador de WhatsApp existente **não foi tocado**. Foram adicionados três eventos que faltavam, em um bloco separado: `oferta_click` (cliques nas seções de oferta e no menu), `email_click` e `faq_leitura`.

## O que ficou de fora, de propósito

- **Páginas próprias para cada oferta.** É a maior fragilidade que sobrou: as três ofertas vivem como âncoras dentro da home, então um assistente que cita a página cita uma página que fala de tudo. É a Prioridade 1 do `CONTENT-PLAN.md`, mas é criação de conteúdo novo e precisa da sua decisão.
- **Limpeza das imagens pesadas.** Existem onze arquivos acima de 300 KB no repositório, o maior com 9,6 MB. Nenhuma página os carrega, então não afetam a velocidade, mas ocupam espaço e podem ser servidos por link direto.
- **Hierarquia de headings.** Todas as páginas pulam de H2 para H4. Corrigir mexe em CSS de várias seções e o ganho é pequeno. Fica registrado na auditoria.
- Qualquer dado listado em `BUSINESS-DATA-NEEDED.md`.

## Prova de que está tudo certo

```bash
python3 docs-geo/seo-tests.py
```

Resultado nesta rodada: **183 PASS, 0 WARN, 0 FAIL.**

## Segunda rodada, 30 de julho de 2026

Feita depois das respostas do proprietário.

**As três ofertas ganharam página própria.** Era a maior fragilidade que tinha sobrado: eVc, IAieu+ e GO viviam como âncoras dentro da home, então um assistente que citasse a página citava uma página que falava de tudo. Agora existem `iaieu-evc.html`, `iaieu-mais.html` e `iaieu-go.html`, cada uma com resposta direta na primeira frase, o texto aprovado da home reaproveitado sem reescrita, uma seção "como funciona" em passos, FAQ própria espelhada no schema, CTA de WhatsApp com mensagem específica e links para os outros dois formatos. O `Service` de cada oferta agora aponta `url` para a sua própria página, na home e na página de ofertas.

**Ligação interna refeita.** A home ganhou três links "ver como funciona" ao lado dos botões existentes. A página "O que vendemos" ganhou um bloco com os três formatos. O rodapé de todas as páginas passou a apontar para as páginas novas em vez das âncoras `index.html#evc`, `#mais` e `#go`. Uma dessas âncoras, a `#go`, estava sendo linkada de três páginas e não existia mais na home: era link quebrado.

**Dados do proprietário gravados.** `foundingDate` 2026. Nome oficial da marca passou a ser "IAieu" apenas, e o `alternateName` "IAieu eVc" foi removido do schema porque eVc é nome de oferta. Nenhum canal de YouTube.

**Isca na voz dele.** Nova seção visível na home, "Quem está falando com você", logo antes do CTA final: mais de três décadas construindo operações e recuperando negócios, em setores e países diferentes, terminando com o convite "me conta em duas linhas o que está travado. Se eu não for a pessoa certa para o seu caso, eu digo na primeira conversa". Nenhum fato novo foi inventado: tudo vem do texto que ele mesmo já publicou em `sobre.html`. A mesma experiência entrou na descrição da pessoa no schema, que antes era genérica.

**Bateria de testes:** 12 páginas monitoradas, **231 PASS, 0 WARN, 0 FAIL**.
