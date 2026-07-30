# Auditoria GEO + SEO do iaieu.com

Executada em 30 de julho de 2026, sobre o commit `073d1c8` publicado em produção.

Legenda: **OK** já está certo, **CORRIGIR** foi encontrado com defeito, **ADICIONAR** não existe e precisa ser criado, **N/A** não se aplica a este negócio.

## Resumo em uma frase

O site é tecnicamente saudável na base (HTML estático, conteúdo todo no HTML bruto, GA4 ativo, bots de IA liberados), mas é **invisível como entidade**: não existe um único bloco de dados estruturados no site inteiro, nenhuma página tem canonical, e a imagem de compartilhamento da home aponta para um arquivo que foi apagado.

## Os três achados que mais pesam

1. **`og:image` da home retorna 404.** A home aponta para `https://iaieu.com/site4.png`, arquivo que virou `.webp` na otimização de imagens e não existe mais. Hoje, todo link do iaieu.com compartilhado no WhatsApp, LinkedIn ou Instagram aparece **sem imagem**. É o defeito de maior impacto imediato e o mais barato de corrigir.
2. **Zero dados estruturados.** Nenhuma das nove páginas tem JSON-LD. Para um assistente de IA, hoje o IAieu é texto solto: não há afirmação legível por máquina de que existe uma organização, um fundador, três serviços e um portfólio.
3. **Zero canonical.** Nenhuma página declara sua própria URL oficial. Com GitHub Pages servindo a home em `/` e em `/index.html`, isso é duplicação de conteúdo esperando para acontecer.

## Tabela dos 28 itens

| # | Item | Status | O que foi encontrado |
|---|---|---|---|
| 1 | Framework e build | OK | HTML estático puro, sem webpack ou gulp. Publicação por commit e push. |
| 2 | Rotas e estrutura | OK | Sete páginas na raiz mais dois subsites. Nenhuma rota quebrada. |
| 3 | Renderização | OK | Conteúdo essencial presente no HTML bruto. `curl` na home retorna a frase de posicionamento. Nada depende de JavaScript para ser lido. |
| 4 | `html lang` | OK | Todas as nove páginas declaram `lang="pt-BR"`. |
| 5 | Title por página | OK | Todos únicos e descritivos, exceto o subsite STW (ver item 22). |
| 6 | Meta description | CORRIGIR | Presentes e boas nas sete páginas da raiz. **Faltando em `stw-daryl-lucas/index.html`.** |
| 7 | Canonical | ADICIONAR | **Nenhuma página tem.** Zero de nove. |
| 8 | `og:image` | CORRIGIR | Home aponta para `site4.png`, que retorna **404**. As outras seis usam `og-image.png` (1200x630, existe, correto). Subsites não têm nenhuma. |
| 9 | Dimensões de `og:image` | CORRIGIR | Só a home declara, e com os valores do arquivo antigo (1672x941). As demais não declaram. |
| 10 | `og:site_name` | ADICIONAR | Ausente em todas as páginas. |
| 11 | `og:locale` | ADICIONAR | Ausente em todas. Precisa ser `pt_BR`. |
| 12 | Twitter Cards | CORRIGIR | Só `twitter:card` está presente. Faltam `twitter:title`, `twitter:description` e `twitter:image`. |
| 13 | JSON-LD | ADICIONAR | **Nenhum bloco em nenhuma página.** Este é o item de maior peso para GEO. |
| 14 | H1 único | CORRIGIR | Uma por página em oito das nove. **O subsite STW tem dois H1.** |
| 15 | Hierarquia de headings | CORRIGIR | Todas as páginas pulam de `h2` para `h4`. Não é grave, mas atrapalha leitores de tela e a leitura estrutural por máquina. |
| 16 | Alt text | OK | Zero imagens sem `alt` nas nove páginas, incluindo as 34 do subsite STW. |
| 17 | Links internos | OK | Menu consistente nas sete páginas. Nenhum link interno quebrado (as três ocorrências detectadas são strings de template em JavaScript, não links reais). |
| 18 | Páginas órfãs | CORRIGIR | `admin.html` não é linkada por nenhuma página, **mas responde 200 em produção e não tem `noindex`**. É um painel interno exposto ao rastreamento. |
| 19 | robots.txt | CORRIGIR | Existe e aponta o sitemap corretamente, mas é genérico. Não declara os bots de IA nem bloqueia `admin.html` e `docs-geo/`. |
| 20 | Bots de IA no CDN | OK | Testado com `curl`: GPTBot responde 200, ClaudeBot responde 200. O GitHub Pages não bloqueia. |
| 21 | sitemap.xml | CORRIGIR | Sete URLs corretas, mas `lastmod` de todas está congelado em 2026-07-25, anterior a duas publicações. Faltam os dois subsites (decisão do proprietário: são portfólio). |
| 22 | Subsites de portfólio | CORRIGIR | `/plinio/` tem title e description mas nada de canonical, OG ou schema. `/stw-daryl-lucas/` está pior: sem description, dois H1 e **dois travessões no título**, o que viola a regra da casa. |
| 23 | Imagens pesadas | CORRIGIR | `FLYER_curso_IAieu.png` tem **9,6 MB**. Mais dez arquivos acima de 300 KB, entre eles `cae-hero-pb.png` e `cae-avatar-iaieu.png` com 1,7 MB cada. A home já foi otimizada e não os carrega, mas eles seguem no repositório e podem ser servidos. |
| 24 | Core Web Vitals | PENDENTE | A home foi otimizada de 14,77 MB para 1,05 MB e validada sem travamentos. Falta o baseline formal do Lighthouse mobile, registrado em `TESTING-CHECKLIST.md`. |
| 25 | Acessibilidade | CORRIGIR | Boa base: `alt` em tudo, `aria-label` nos controles do carrossel, foco visível. Pendências: hierarquia de headings (item 15) e ausência de link "pular para o conteúdo". |
| 26 | Consistência de dados | CORRIGIR | O WhatsApp é idêntico em todas as páginas. Mas o e-mail comercial não aparece em lugar nenhum do site, e os perfis sociais estão incompletos: só o Instagram da marca, sem LinkedIn. |
| 27 | Página 404 | ADICIONAR | Não existe `404.html`. O GitHub Pages entrega a página genérica dele, fora da identidade do site. |
| 28 | Avaliações e provas | OK | Nenhum `aggregateRating` ou `Review` inventado. Os depoimentos são reais e exibidos como imagem. Regra mantida: **nunca** criar avaliação própria. |

## Itens que não se aplicam

Estes fazem parte do processo original, que foi desenhado para um negócio local, e foram descartados de propósito porque o IAieu não é um:

- `LocalBusiness` e `areaServed` com cidades
- Páginas de cidade
- Google Business Profile e Bing Places
- Consistência de NAP (nome, endereço, telefone). No lugar dela entra o `CONSISTENCY-CHECKLIST.md`, que checa consistência de identidade entre site, LinkedIn, Instagram e materiais de venda.

## O que depende do proprietário

Está tudo consolidado em `BUSINESS-DATA-NEEDED.md`. Os itens que travam decisão técnica são poucos: o ano de fundação do IAieu, a confirmação do nome público oficial (com ou sem "Marc") e a existência de canal no YouTube.
