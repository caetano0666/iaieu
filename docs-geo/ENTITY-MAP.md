# Mapa de entidades do IAieu

Gerado em 30 de julho de 2026. Fonte dos dados: `business.json`.

Este documento define **quem é quem** para os buscadores e assistentes de IA. Cada entidade tem um `@id` estável: um endereço fixo que nunca muda, mesmo que o texto da página mude. É isso que permite a uma máquina entender que a "IAieu" citada na página de projetos é a mesma da home.

## Decisão central: duas entidades, não uma

O IAieu é uma operação de uma pessoa só. Mesmo assim, mantemos **Organization e Person separados**, ligados por `founder` e `worksFor`.

Motivo: em consultoria, a pessoa carrega tanta autoridade quanto a marca. Quem pergunta a um assistente "quem me ajuda a usar IA no meu negócio" busca uma pessoa confiável. Quem pergunta "o que é o IAieu" busca a marca. Fundir as duas entidades faria o site responder bem a uma pergunta e mal à outra. Separadas e ligadas, cada uma responde à sua.

## Identificadores estáveis

| @id | Tipo | O que representa |
|---|---|---|
| `https://iaieu.com/#organization` | Organization | A marca IAieu |
| `https://iaieu.com/#person-caetano` | Person | Caetano Zammataro, fundador |
| `https://iaieu.com/#website` | WebSite | O site como um todo |
| `https://iaieu.com/#webpage` | WebPage | A home |
| `https://iaieu.com/o-que-vendemos.html#webpage` | WebPage | Página de ofertas |
| `https://iaieu.com/sobre.html#webpage` | AboutPage | Página sobre |
| `https://iaieu.com/projetos.html#webpage` | CollectionPage | Página de projetos |
| `https://iaieu.com/conteudos.html#webpage` | CollectionPage | Curadoria |
| `https://iaieu.com/arte.html#webpage` | CollectionPage | Galeria |
| `https://iaieu.com/depoimentos.html#webpage` | WebPage | Depoimentos |
| `https://iaieu.com/#service-evc` | Service | Oferta IAieu eVc |
| `https://iaieu.com/#service-mais` | Service | Oferta IAieu+ |
| `https://iaieu.com/#service-go` | Service | Oferta IAieu GO |
| `https://iaieu.com/#work-plinio` | CreativeWork | Site do acervo Plínio Marcos |
| `https://iaieu.com/#work-stw` | CreativeWork | Site Sparta Team Wear |
| `https://iaieu.com/#faq` | FAQPage | Perguntas frequentes da home |

Regra: o `@id` usa sempre a URL canônica da página mais um fragmento (`#`). Nunca inventar um `@id` novo para uma entidade que já existe: referenciar o `@id` existente.

## Como as entidades se ligam

```
Organization (IAieu)
  ├── founder ──────────────► Person (Caetano Zammataro)
  ├── logo ─────────────────► logo_horizontal.png
  ├── sameAs ───────────────► Instagram @iaieu.evc
  ├── contactPoint ─────────► WhatsApp e e-mail
  └── makesOffer ───────────► Service eVc, Service +, Service GO

Person (Caetano Zammataro)
  ├── worksFor ─────────────► Organization (IAieu)
  ├── jobTitle ─────────────► Fundador do IAieu
  ├── knowsAbout ───────────► competências reais (ver business.json)
  ├── knowsLanguage ────────► pt-BR apenas
  └── sameAs ───────────────► LinkedIn, Instagram pessoal

WebSite
  ├── publisher ────────────► Organization
  ├── inLanguage ───────────► pt-BR
  └── (sem SearchAction: o site não tem busca interna)

Cada WebPage
  ├── isPartOf ─────────────► WebSite
  ├── about / mainEntity ───► Organization ou Person, conforme a página
  └── breadcrumb ───────────► BreadcrumbList

CreativeWork (Plínio, STW)
  └── creator ──────────────► Organization (IAieu)
```

## Por que cada perfil está onde está

O proprietário confirmou três perfis em 30 de julho de 2026:

- **Instagram @iaieu.evc** fica no `sameAs` da **Organization**: é o perfil da marca.
- **LinkedIn caetano-marc-zammataro** e **Instagram @caetano.zammataro** ficam no `sameAs` da **Person**: são perfis pessoais.

Trocar isso de lugar confunde a máquina: um `sameAs` errado afirma que a marca e a pessoa são o mesmo perfil, e é exatamente a distinção que estamos tentando preservar.

## O que ficou de fora de propósito

| Não usado | Motivo |
|---|---|
| `LocalBusiness` | O IAieu não é negócio local. Não tem endereço de atendimento nem área geográfica de serviço. |
| `areaServed` com cidades | Mesmo motivo. O alcance é Brasil e falantes de português no exterior. |
| `aggregateRating` e `Review` | Regra absoluta: nunca criar avaliação própria. Os depoimentos do site são reais, mas não viram nota. |
| `SearchAction` no WebSite | O site não tem busca interna. Declarar seria mentira estrutural. |
| `Offer` com `price` | Decisão do proprietário: preços não são públicos. Um `Offer` sem preço é permitido e honesto. |
| `foundingDate` | Não confirmado. Está em `BUSINESS-DATA-NEEDED.md`. |
| `knowsLanguage` além de pt | Inglês e espanhol não confirmados pelo proprietário. |

## Subsites de portfólio

Decisão do proprietário em 30 de julho de 2026: `/plinio/` e `/stw-daryl-lucas/` são **vitrine do IAieu**, não projetos independentes.

Consequências práticas:
1. Entram no `sitemap.xml` do iaieu.com.
2. Aparecem no grafo como `CreativeWork` com `creator` apontando para `https://iaieu.com/#organization`.
3. Ganham canonical próprio e metadata completa, porque agora são porta de entrada do site.
4. **Não** recebem o schema de Organization do IAieu na própria página: eles falam de Plínio Marcos e da Sparta Team Wear, não do IAieu. O vínculo é feito a partir de `projetos.html`.
