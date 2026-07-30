# Inventário de dados estruturados

Estado após a implementação de 30 de julho de 2026. Antes dela, o site tinha **zero** blocos de dados estruturados.

Cada página tem exatamente um bloco `<script type="application/ld+json">` com um `@graph`. Um bloco só por página evita entidades duplicadas e conflito de `@id`.

## Por página

| Página | Entidades no grafo | Tipos |
|---|---|---|
| `index.html` | 8 | Organization, Person, WebSite, Service x3, WebPage, FAQPage |
| `o-que-vendemos.html` | 4 | Service x3, WebPage com ItemList |
| `sobre.html` | 2 | Person, AboutPage |
| `projetos.html` | 3 | CreativeWork x2, CollectionPage com ItemList |
| `conteudos.html` | 1 | CollectionPage |
| `arte.html` | 1 | CollectionPage |
| `depoimentos.html` | 1 | WebPage |
| `plinio/index.html` | 2 | CreativeWork, WebPage |
| `stw-daryl-lucas/index.html` | 2 | CreativeWork, WebPage |

## Campos declarados na Organization

`name`, `alternateName`, `url`, `logo`, `image`, `slogan`, `description`, `email`, `founder`, `knowsLanguage`, `sameAs`, `contactPoint`, `makesOffer`.

## Campos declarados na Person

`name`, `jobTitle`, `description`, `url`, `worksFor`, `knowsAbout` (cinco competências reais), `knowsLanguage`, `sameAs` (LinkedIn e Instagram pessoal).

## O que está proibido e é testado automaticamente

O `seo-tests.py` falha a bateria inteira se qualquer um destes aparecer:

| Proibido | Motivo |
|---|---|
| `aggregateRating`, `reviewRating`, `ratingValue` | Nunca criar avaliação própria. Os depoimentos do site são reais, mas não viram nota. |
| `"price"` | Preços não são públicos por decisão do proprietário. |
| `LocalBusiness` | O IAieu não é negócio local. |
| `@id` fora de `https://iaieu.com` | `@id` precisa ser estável e do próprio domínio. |
| `@id` com tipos divergentes entre páginas | O mesmo identificador não pode ser Organization numa página e outra coisa em outra. |

## Detalhes que valem explicação

**Offer sem preço.** Cada `Service` tem um `Offer` com `availability` e `priceCurrency`, mas nenhum `price`. Isso é válido em Schema.org e é honesto: afirma que o serviço está disponível sem afirmar um valor que não é público.

**FAQPage espelhada 1:1.** As sete perguntas do schema existem como texto visível na home, palavra por palavra. O teste `teste_faq_espelhada` compara pergunta e resposta contra o texto visível da página e falha se alguma só existir no schema. Isso evita a prática, penalizada, de declarar FAQ que o visitante não vê.

**Sem `SearchAction`.** O site não tem busca interna. Declarar seria uma afirmação falsa sobre a estrutura do site.

**Subsites não carregam a Organization do IAieu.** As páginas de Plínio Marcos e Sparta Team Wear falam desses assuntos, não do IAieu. Elas declaram a obra (`CreativeWork`) com `creator` apontando para o `@id` da Organization. O vínculo de portfólio é afirmado a partir de `projetos.html`, onde ele é verdadeiro.

## Como validar manualmente

1. Teste de resultados avançados do Google: https://search.google.com/test/rich-results
2. Validador do Schema.org: https://validator.schema.org/
3. Cole a URL da página ou o HTML. Espere zero erro. Avisos sobre campos recomendados que decidimos não preencher (preço, por exemplo) são esperados e aceitáveis.
