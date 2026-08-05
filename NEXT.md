# NEXT

## Missão

Construir um sistema de trabalho com IA que funcione mesmo quando eu esquecer onde parei.

---

# STATUS DO PROJETO — IAieu V3 Final

**Data: 04/08/2026**

## O que foi concluído

A fase de direção de criação do site foi oficialmente encerrada.

Durante este ciclo, o projeto deixou de ser um site sobre inteligência artificial para se tornar uma marca baseada em experiência operacional.

O objetivo deixou de ser explicar tecnologia. Passou a ser organizar problemas complexos com clareza, utilizando tecnologia apenas quando ela faz sentido.

## Principais conquistas

- Posicionamento consolidado.
- Hero definitiva.
- Linguagem editorial definida.
- Arquitetura estabilizada.
- Home editada e reduzida em aproximadamente 15% sem perda de conteúdo.
- Voz institucional unificada.
- Sistema visual consolidado.
- Regras permanentes registradas.
- Auditorias técnicas e editoriais concluídas.
- Publicação validada.

## Regras permanentes

### Voz

- "Eu" para ações executadas pelo Caetano.
- "IAieu" para método, filosofia e marca.
- Plural apenas quando incluir genuinamente o cliente.

### Geometria

- Cards: 18px.
- Tags: pílula.
- Círculos apenas quando realmente forem círculos.

Nunca criar novas geometrias apenas para variar a interface.

### Promessa

Nunca prometer transformar uma operação antes de conhecê-la.

O IAieu melhora processos. Não julga operações.

## Filosofia da marca

O IAieu não explica inteligência artificial.

**O IAieu reduz complexidade antes que ela se transforme em ansiedade.**

## Estado do projeto

O site deixa de ser um projeto em desenvolvimento. Passa a ser um produto em operação.

A partir deste momento, nenhuma alteração deve nascer apenas de opinião estética.

As próximas evoluções deverão surgir de:

- casos reais;
- comportamento dos visitantes;
- dúvidas recorrentes;
- novos conteúdos;
- amadurecimento natural da marca.

## Próximo capítulo

O foco deixa de ser o site. O foco passa a ser construir autoridade editorial.

A marca será fortalecida por: artigos, estudos de caso, apresentações, vídeos, palestras, LinkedIn, Instagram e experiência publicada.

---

# Anexo técnico

Escrito para quem abrir este arquivo daqui a um ano e precisar mexer sem quebrar nada.

## Onde as coisas moram

| O quê | Onde |
|---|---|
| Site publicado | `/Users/cae/IAieu-site`, único ambiente com Git. Publica por commit e push na `main` |
| Fonte única de verdade | `docs-geo/business.json`. Dado que não está lá não pode ir para o site |
| Regras invioláveis, com o motivo de cada uma | `docs-geo/FUTURE-MAINTENANCE.md` |
| Bateria de testes | `python3 docs-geo/seo-tests.py`, obrigatório **0 FAIL** antes de publicar |
| CSS da evolução visual da home | Blocos marcados no fim do `<style>` do `index.html`: V2, V2.2 e a regra permanente de forma. Apagar um bloco devolve o estado anterior |
| CSS das páginas internas | Fim do `estilo.css`, compartilhado pelas nove |

## Armadilhas conhecidas

**O `.gitignore` bloqueia tudo por padrão.** Arquivo novo do site precisa ser liberado de propósito na lista de permissão. Isso já causou uma página publicada sem o arquivo, em 404, por alguns minutos.

**O Git trava com locks presos.** Aconteceu duas vezes. Conferir que nenhum processo git está rodando e remover os arquivos `.lock` de dentro do `.git`.

**Antes de aplicar raio de canto a um seletor múltiplo, conferir se todos os elementos são da mesma natureza.** Cartão e etiqueta nunca compartilham raio. Foi esse descuido que transformou os cartões do método em cápsulas.

**Auditoria de texto não pega tudo.** O título do posicionamento antigo sobreviveu a quatro auditorias dentro do campo `name` do JSON-LD, porque todas conferiam o texto visível e a tag `<title>`. Conferir o schema por dentro.

## O que ficou aberto, e nenhum deles é trabalho de site

1. **Segundo caso operacional**, com antes e depois medido de um cliente externo. Hoje existe um caso só, e o cliente dele foi o próprio IAieu.
2. **Página de Conteúdos** promete oito temas e entrega dois posts. É a página mais fraca do site.
3. **Fotografia.** A atual mostra o homem e não mostra o trabalho. Briefing definido: mesma chave baixa, mesmo preto, mesma sobriedade, e uma prova visual de que esse homem trabalha.
4. **Rosa dos Ventos.** Decidido esperar em vez de usar como enfeite. Conceito proposto e não implementado: ela não aparece desenhada, ela é a razão de a luz existir na fotografia.
5. **Apresentação da IGP Sports** ainda assina "Instituto IAieu" no último slide.
6. **Bio do Instagram e LinkedIn** provavelmente ainda falam do posicionamento antigo.
7. Cinco regras de CSS órfãs das etiquetas removidas na edição final. Não afetam nada.

## O que aconteceu no dia 04/08/2026

| Hora | Commit | O que foi |
|---|---|---|
| 10:35 | `0c0a599` | V2: evolução da direção de arte em todas as páginas |
| 19:52 | `3af707e` | V2.2: áreas claras, costura entre seções, card do Google, nova pergunta, promessa revista, a letra escorregada em "retrabalho" |
| 20:58 | `f5f7617` | V3: maturidade editorial, quase toda subtração |
| 21:06 | `57ef7ff` | V3.1: uma lógica de voz para toda a marca |
| 21:08 | `5c3e461` | Schema da home: título antigo que sobreviveu ao reposicionamento |
| 21:09 | `54a5caa` | Texto alternativo da imagem de compartilhamento |
| 21:15 | `4c9d31e` | Reverte cartões em cápsula e cria a regra permanente de forma |
| 21:34 | `bc18639` | Edição final: 14,7% a menos na home, sem perda de conteúdo |

Estado dos testes ao fim do dia: **232 PASS, 0 WARN, 0 FAIL.**

A história completa das decisões anteriores, com o motivo de cada uma, está nos PDFs da pasta `LOG` em `/Users/cae/iaieu/LOG/`.
