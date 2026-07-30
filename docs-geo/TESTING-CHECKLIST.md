# Checklist de testes

## Antes de todo deploy, sem exceção

```bash
python3 docs-geo/seo-tests.py
```

Precisa terminar em **0 FAIL**. Se falhar, não publique: corrija primeiro. Um WARN não bloqueia, mas precisa ser uma decisão consciente.

Estado em 30 de julho de 2026: **183 PASS, 0 WARN, 0 FAIL**.

## O que a bateria cobre

| Grupo | Verificações |
|---|---|
| Arquivos críticos | CNAME, robots.txt, sitemap.xml e o arquivo de verificação do Google existem |
| Metadata | title e description únicos e presentes, canonical autorreferente, og:site_name, og:locale, og:image absoluta **e o arquivo existindo de verdade**, twitter card, lang pt-BR |
| Estrutura | exatamente um H1 por página, nenhuma imagem sem alt |
| Dados estruturados | JSON-LD parseável, WebPage declarada, url do WebPage igual ao canonical, breadcrumb, `@id` estável e do domínio, sem tipo divergente |
| Regras absolutas | nenhum aggregateRating, nenhum campo price, nenhum LocalBusiness |
| Entidades da home | Organization, Person, WebSite e FAQPage presentes; founder e worksFor ligados nos dois sentidos |
| FAQ | as sete perguntas e respostas do schema existem como texto visível |
| Conteúdo | conteúdo essencial presente no HTML bruto de cada página |
| Regras da casa | zero travessão, palavras de jargão fora do texto visível |
| Infra | sitemap sem duplicata nem lixo e com lastmod válido, robots com os bots de IA e bloqueios certos, admin com noindex, chave IndexNow consistente, llms.txt com aviso e sem preço |

## Verificação manual após publicar

1. **A imagem de compartilhamento aparece?** Cole `https://iaieu.com` no WhatsApp, sem enviar. A prévia precisa mostrar a imagem. Este item existe porque a home ficou com a imagem quebrada por dias sem ninguém notar.
2. **Dados estruturados sem erro:** https://search.google.com/test/rich-results com a URL da home.
3. **Bots de IA conseguem ler:**
```bash
curl -s -A "GPTBot" -o /dev/null -w "%{http_code}\n" https://iaieu.com/
```
Espere 200.
4. **Arquivos novos no ar:** `https://iaieu.com/llms.txt`, `https://iaieu.com/robots.txt`, `https://iaieu.com/404.html` e um endereço inventado qualquer para ver a página 404 na identidade do site.
5. **Search Console:** pedir indexação da home e das páginas que mudaram.

## Baseline de performance

Registre aqui o resultado do Lighthouse mobile a cada rodada, para comparar depois. Como medir sem instalar nada: abra https://pagespeed.web.dev/, cole a URL, escolha a aba Mobile.

| Data | Página | Performance | Acessibilidade | Boas práticas | SEO | LCP | CLS |
|---|---|---|---|---|---|---|---|
| a preencher | Home | | | | | | |
| a preencher | O que vendemos | | | | | | |
| a preencher | Sobre | | | | | | |

Contexto conhecido: a home foi de 14,77 MB para 1,05 MB em julho de 2026 e passou por três varreduras de rolagem sem travamento. Existem imagens pesadas ainda no repositório que nenhuma página carrega, sendo a maior o `FLYER_curso_IAieu.png` com 9,6 MB. Elas não afetam a nota, mas convém limpar.

## Pendências de teste que dependem de outra máquina

| Item | Por quê |
|---|---|
| Confirmação em tela retina (DPR 2) | O ambiente de verificação automatizada roda em DPR 1. |
| Throttle de CPU 4x no DevTools | Precisa ser feito no navegador do proprietário. |
| Teste com 2 ou 3 pessoas do público real | Nenhuma ferramenta substitui isso. |
