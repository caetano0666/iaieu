# Manutenção futura: regras anti-regressão

Este arquivo existe para uma coisa só: impedir que o trabalho já feito seja desfeito sem querer numa alteração futura. Quem for mexer no site iaieu.com, seja pessoa ou assistente de IA, lê este arquivo antes.

Regressão é quando alguma coisa que estava funcionando volta a quebrar. Costuma acontecer sem má intenção, no meio de uma alteração aparentemente inofensiva.

---

## 1. Arquivos que NUNCA podem ser apagados, renomeados ou movidos

Estes quatro arquivos ficam na raiz do site. Raiz é a pasta principal, a mesma onde está o `index.html`.

| Arquivo | Para que serve | O que acontece se sumir |
|---|---|---|
| `CNAME` | Diz ao GitHub Pages que o site atende pelo endereço `iaieu.com` | O domínio para de funcionar. O site sai do ar no endereço próprio |
| `robots.txt` | Autoriza os buscadores a ler o site e aponta o sitemap | Os buscadores perdem a referência do sitemap. Se o conteúdo for trocado por `Disallow: /`, o site some da busca |
| `sitemap.xml` | Lista todas as páginas do site para os buscadores | Google e Bing perdem o mapa. Páginas novas demoram muito mais para ser descobertas |
| `google7279386773b5d258.html` | Prova para o Google que o dono do site é você | A verificação do Search Console cai. Todo o histórico do painel fica inacessível |

Regras práticas:

- Não abra esses arquivos para "arrumar a formatação".
- Não mude o nome de nenhum deles, nem para deixar mais bonito.
- Não os coloque dentro de uma subpasta. Eles têm que ficar na raiz.
- Se algum sistema de publicação avisar que vai remover arquivos "não usados", pare e confira essa lista antes de confirmar.
- Se a chave do IndexNow for criada (veja `BING-WEBMASTER-SETUP.md`), o arquivo `.txt` dela entra nesta mesma lista.

Como conferir em 30 segundos que os quatro estão vivos: abra estes endereços no navegador, um por um.

```
https://iaieu.com/robots.txt
https://iaieu.com/sitemap.xml
https://iaieu.com/google7279386773b5d258.html
```

Os três precisam abrir sem erro. O `CNAME` não abre pelo navegador, confira a existência dele na pasta do projeto.

---

## 2. Antes de todo deploy: rodar o teste e exigir 0 FAIL

Deploy é o ato de publicar as alterações e deixar o site novo no ar.

**Regra: nenhum deploy acontece sem rodar `docs-geo/seo-tests.py` e obter 0 FAIL.**

Como rodar:

1. Abra o aplicativo `Terminal` no Mac.
2. Digite `cd ` (com espaço no fim) e arraste a pasta do projeto para dentro da janela do Terminal. Aperte Enter.
3. Digite o comando abaixo e aperte Enter:

```
python3 docs-geo/seo-tests.py
```

4. Leia a saída. Ela lista cada checagem com `PASS` ou `FAIL`, e no final mostra o total.
5. Decisão:

| Resultado | O que fazer |
|---|---|
| 0 FAIL | Pode publicar |
| 1 FAIL ou mais | **Não publique.** Corrija o que o teste apontou e rode de novo |

Não existe FAIL aceitável. Não existe "esse FAIL é bobagem". Se um teste virou bobagem, a decisão é remover o teste de forma consciente e documentada, não ignorar o resultado dele.

---

## 3. Ao criar uma página nova: itens obrigatórios

Toda página nova do iaieu.com precisa ter os sete itens abaixo antes de ir ao ar. Falta de qualquer um é motivo para segurar a publicação.

| # | Item | Regra |
|---|---|---|
| 1 | `<title>` único | Nenhuma outra página do site pode ter o mesmo título. Padrão em uso: `Nome da página · IAieu` |
| 2 | `description` única | A meta description precisa ser escrita para aquela página. Copiar de outra página é erro |
| 3 | `canonical` próprio | A tag canonical tem que apontar para o endereço da própria página, não para a home. Exemplo: numa página `pagina-nova.html`, o canonical é `https://iaieu.com/pagina-nova.html` |
| 4 | `og:image` absoluta | O endereço da imagem de compartilhamento precisa começar com `https://iaieu.com/`. Caminho curto tipo `og-image.png` não funciona quando o link é compartilhado |
| 5 | Um H1 só | Exatamente um `<h1>` na página. Nem zero, nem dois |
| 6 | Entrada no `sitemap.xml` | Adicionar o bloco `<url>` da página nova, com `lastmod` na data real da publicação, no formato `AAAA-MM-DD`. Data inventada ou data futura é pior que não ter data |
| 7 | JSON-LD de `WebPage` | Bloco de dados estruturados do tipo `WebPage`, ligado aos `@id` já definidos na home, para as entidades de organização, pessoa e site. A página nova não cria entidades novas, ela referencia as que já existem |

Sobre o item 7, em linguagem simples: a home é o registro central que diz quem é a marca, quem é a pessoa e qual é o site. Cada página nova só aponta para esses registros, em vez de repetir a informação. Se cada página inventar sua própria descrição de organização, os buscadores passam a ver várias marcas diferentes em vez de uma.

Ordem recomendada ao criar página nova:

1. Escrever a página com os itens 1 a 5 e o item 7.
2. Adicionar a linha no `sitemap.xml` com a data real (item 6).
3. Rodar `python3 docs-geo/seo-tests.py` e exigir 0 FAIL.
4. Publicar.
5. Pedir indexação no Search Console, conforme `SEARCH-CONSOLE-SETUP.md`.
6. Se o IndexNow já estiver ativo, disparar o ping, conforme `BING-WEBMASTER-SETUP.md`.

---

## 4. Regra de datar números e resultados

Todo número de cliente, resultado, tempo de mercado ou volume publicado no site precisa vir com a data em que aquilo era verdade, no formato `em [mês ano]`.

Certo:
- `Mais de 40 pessoas atendidas em julho 2026.`
- `Projeto entregue em março 2026.`

Errado:
- `Mais de 40 pessoas atendidas.`
- `Já atendemos centenas de clientes.`
- `Anos de experiência.`

Motivos: número sem data envelhece sozinho e vira mentira sem que ninguém perceba. Além disso, buscadores e assistentes de IA tratam melhor uma afirmação que se pode situar no tempo. E, se alguém questionar, a data é a defesa.

Regra complementar: se o número não pode ser comprovado, ele não vai para o site. Não arredonde para cima.

---

## 5. Nunca criar `aggregateRating` nem `review` por conta própria

`aggregateRating` é o dado estruturado que produz aquelas estrelinhas de nota nos resultados de busca. `review` é a avaliação individual.

**Não crie nenhum dos dois no site do IAieu sem uma decisão explícita e um processo de coleta real de avaliações.**

Por quê:

1. O Google trata nota inventada como manipulação. A penalidade não é só perder as estrelinhas, pode afetar a confiança no site inteiro.
2. Para ser legítimo, o dado precisa vir de avaliações reais, coletadas de forma verificável, e visíveis na própria página para qualquer visitante.
3. Depoimento em vídeo ou em texto na página de depoimentos é ótimo e é permitido. O que não é permitido é converter isso em uma nota numérica no código.

Se um assistente de IA, um plugin ou um consultor sugerir "adicionar aggregateRating para ganhar estrelinhas", a resposta é não. Registre a sugestão e leve para decisão consciente, não implemente.

---

## 6. Textos de posicionamento aprovados: não reescrever

Os textos abaixo foram decididos e não mudam em alteração de rotina:

- A frase de posicionamento: `Seu problema não está sem solução. Está sem direção.`
- Os títulos e descrições atuais das páginas publicadas.
- Os nomes das ofertas: `IAieu eVc`, `IAieu+`, `IAieu GO`.
- A descrição curta oficial, nas versões de uma e de três linhas, registrada em `CONSISTENCY-CHECKLIST.md`.

Regras:

- Não reescreva por gosto pessoal, nem para "melhorar o SEO", nem para caber melhor no layout.
- Mudança nesses textos só acontece por decisão do Caetano, e quando acontece precisa mudar em todos os canais no mesmo dia, seguindo `CONSISTENCY-CHECKLIST.md`.
- Nunca publique preço em nenhuma página. Preço vai em proposta individual.

---

## 7. Regra de escrita: zero travessão

Em todo texto publicado no site, e em toda documentação desta pasta, **não se usa travessão**.

O travessão é o traço longo, o caractere que aparece em construções do tipo "isto, aquilo e também isto". Em vez dele, use:

| Em vez de travessão | Use |
|---|---|
| Separar uma explicação no meio da frase | Vírgulas |
| Introduzir uma explicação no fim da frase | Dois-pontos |
| Emendar duas ideias | Ponto final e uma frase nova |

Como conferir antes de publicar, no Terminal, dentro da pasta do projeto. Copie a linha inteira exatamente como está. O trecho `\u2014` é o código do caractere procurado, assim você não precisa digitá-lo:

```
grep -rn "$(printf '\u2014')" *.html docs-geo/*.md
```

Se o comando não devolver nada, está limpo. Se devolver linhas, cada uma dessas linhas precisa ser corrigida antes de publicar. O teste `seo-tests.py` também cobre essa checagem.

Além do travessão, vale a lista de palavras banidas do IAieu, aquele vocabulário de palestra que não diz nada de concreto. A lista e o critério estão em `docs-geo/CONTENT-PLAN.md`. Regra prática: se a palavra pudesse aparecer no site de qualquer consultoria do mundo sem mudar nada, ela não serve. Diga a coisa concreta que acontece com a pessoa.

Duas coisas que nunca se promete, em nenhum texto, em nenhuma proposta:

1. Posição no Google.
2. Citação garantida em assistente de IA.

Ambas dependem de decisões de terceiros que ninguém controla. Prometer isso é vender o que não se pode entregar.

---

## 8. Quando algo quebrar

Tabela de primeiros socorros. Ache o sintoma na coluna da esquerda e faça o que está na coluna da direita, nessa ordem.

| Sintoma | Primeira coisa a checar |
|---|---|
| O site não abre em `iaieu.com`, mas abre no endereço do GitHub | O arquivo `CNAME` sumiu da raiz ou teve o conteúdo alterado. Restaure com o conteúdo `iaieu.com` |
| O Search Console avisa "propriedade não verificada" | O arquivo `google7279386773b5d258.html` sumiu da raiz. Abra `https://iaieu.com/google7279386773b5d258.html`. Se der 404, restaure o arquivo idêntico ao original |
| Todas as páginas viraram "não indexadas" de uma vez | Abra `https://iaieu.com/robots.txt`. Se estiver escrito `Disallow: /`, esse é o problema. Precisa voltar para `Allow: /` |
| Páginas novas nunca aparecem na busca | Abra `https://iaieu.com/sitemap.xml` e confira se a página nova está listada. Se não estiver, falta o item 6 da seção 3 deste arquivo |
| O link compartilhado no WhatsApp ou no LinkedIn aparece sem imagem | A `og:image` daquela página está com endereço relativo. Precisa começar com `https://iaieu.com/` |
| Duas páginas competindo pela mesma busca, e o Google mostra a errada | Os títulos ou as descrições estão iguais ou parecidos demais, ou o canonical de uma aponta para a outra |
| O GA4 parou de registrar visitas | Abra qualquer página do site, veja o código-fonte e confira se o identificador `G-KRMHLHQNGB` ainda está lá. Se a alteração recente mexeu no cabeçalho das páginas, provavelmente o trecho foi removido sem querer |
| O evento `whatsapp_click` sumiu dos relatórios | O link do WhatsApp foi trocado e perdeu o código que dispara o evento. Compare com um link de WhatsApp de outra página que ainda funciona |
| O teste `seo-tests.py` deu FAIL e ninguém entende o motivo | Leia a linha do FAIL, ela nomeia o arquivo e a checagem. Desfaça a última alteração feita e rode de novo. Se passar, o problema está naquela alteração |
| O sitemap aparece com erro no Search Console ou no Bing | Abra `https://iaieu.com/sitemap.xml` no navegador. Se aparecer mensagem de erro de XML, alguma linha ficou malformada. Compare com uma versão anterior do arquivo |
| Um assistente de IA descreve o IAieu de forma errada | Não é quebra técnica. Rode a checagem de `CONSISTENCY-CHECKLIST.md`, quase sempre algum canal está com descrição antiga |

Regra geral para qualquer sintoma desta tabela: a primeira pergunta é sempre **"o que mudou por último?"**. Na enorme maioria dos casos, a resposta está na alteração mais recente, e desfazer é mais rápido que investigar.

---

## 9. Lista final antes de publicar qualquer coisa

- [ ] `CNAME`, `robots.txt`, `sitemap.xml` e `google7279386773b5d258.html` continuam na raiz, intactos.
- [ ] Rodei `python3 docs-geo/seo-tests.py` e obtive 0 FAIL.
- [ ] Se criei página nova, ela tem os 7 itens obrigatórios da seção 3.
- [ ] Se criei página nova, ela está no `sitemap.xml` com `lastmod` na data real.
- [ ] Nenhum número novo foi publicado sem a data no formato `em [mês ano]`.
- [ ] Não criei `aggregateRating` nem `review` no código.
- [ ] Os textos de posicionamento aprovados continuam iguais.
- [ ] Rodei o grep de travessão da seção 7 e não veio nada.
- [ ] Nenhum preço foi publicado.
- [ ] Nenhuma promessa de posição no Google ou de citação em IA foi escrita.


---

## Regra de ouro do reposicionamento (3 de agosto de 2026)

Antes de publicar qualquer texto novo no site, faça uma pergunta: **se uma IA lesse só isto, ela diria que o IAieu é uma empresa de quê?**

Se a resposta for "de inteligência artificial", o texto está errado, mesmo que esteja bonito.

O que o site vende: **soluções operacionais sob medida para empresas e pessoas.** O que sustenta isso: **quarenta anos organizando operações.** O papel da tecnologia: **ferramenta escolhida em função do problema.**

### Nunca escreva no site

- "Instituto IAieu"
- "trinta anos", "três décadas", "30+"
- "alívio" como promessa
- "metodologia", "framework", "método proprietário": o método é o jeito natural de trabalhar, não um produto
- Preço, prazo, garantia ou número de clientes sem confirmação do Caetano
- Travessão

### Sempre que mexer na camada visível, mexa na invisível junto

Texto novo na página exige revisar: title, meta description, open graph, twitter card, schema da página e, se mudar o posicionamento, também `llms.txt` e `docs-geo/business.json`. O `business.json` é a fonte da verdade: se o dado não está lá, ele não pode ir para o site.

### Antes de todo deploy

```bash
python3 docs-geo/seo-tests.py
```

Precisa dar **0 FAIL**. A bateria tem um teste que cobra a frase-tese em cada página principal: se alguém reescrever a home e apagar a tese, o teste quebra de propósito.


---

## Regra editorial da página de Depoimentos (3 de agosto de 2026)

Definida pelo proprietário e vale para sempre:

> **Nenhum depoimento entra porque elogia o Caetano. Todo depoimento entra porque comprova a identidade do IAieu.**

A página não existe para provar que gostam dele. Existe para mostrar que aquilo que o site afirma sobre operação, execução e processo já era percebido por outras pessoas muito antes desta empresa existir.

Na primeira seleção, sete recomendações públicas do LinkedIn foram avaliadas e **quatro entraram**: Andréa Galletti (quatro décadas, com data de 1983), Marcelo Penna (excelência operacional, escrita por um cliente), Vanessa Srna (execução) e Celso Squilanti (processos). **Três ficaram de fora** por serem elogio à pessoa sem prova de operação: Jack Servera, Fábio Melo e Mariana Boff. Não são ruins, são fora de escopo.

Regras de forma, já aplicadas:
- Texto nativo, nunca print de tela. Print é invisível para busca e para IA, e o print do LinkedIn ainda expõe o painel de edição do próprio dono.
- Citação reproduzida ao pé da letra, sem corte e sem correção. **Aqui o travessão é permitido**, porque fidelidade a texto de terceiro vale mais que a padronização da casa.
- Um destaque por depoimento, só no trecho que justifica a presença dele.
- Depoimento em inglês fica em inglês, com tradução discreta abaixo, identificada como tradução.
- Cada bloco leva o vínculo real (foi cliente, trabalhou na mesma equipe) e a data.
- **Nunca criar `Review` ou `aggregateRating` no schema**, mesmo sendo depoimentos verdadeiros.


---

## Voz da marca, definida em 4 de agosto de 2026

O IAieu é conduzido por uma pessoa só, e o texto do site precisa refletir isso.

- **Primeira pessoa do singular** quando a ação é executada pelo Caetano: "eu entro na operação", "eu não vendo ferramentas", "eu mostro como pode funcionar melhor".
- **"O IAieu", "o método" ou "o trabalho"** quando o assunto é a marca, o método ou a filosofia: "o IAieu desenvolve soluções operacionais sob medida".
- **Plural apenas quando inclui o cliente.** "A gente resolve junto", "se gerar valor, seguimos juntos" e "olhar junto" são plurais verdadeiros e devem ser preservados. O plural que finge equipe é proibido.
- **Citação de terceiro nunca se altera**, mesmo contendo plural. Os depoimentos da Andréa e do Marcelo têm "nós" e continuam intactos.

Estado após a auditoria: **zero plural exclusivo em todo o domínio**, incluindo o `llms.txt`.


---

## Regra permanente de forma, 4 de agosto de 2026

Definida pelo proprietário depois de duas ocorrências do mesmo erro.

> **Nunca introduza uma geometria nova apenas para quebrar repetição visual.**
> A variedade do IAieu deve surgir da edição, da composição e do silêncio, nunca de formas decorativas.
> Se uma solução chama mais atenção para o formato do componente do que para a informação que ele contém, ela enfraquece a identidade da marca.

Na prática, o sistema tem **três formas e nenhuma quarta**:

| Elemento | Raio |
|---|---|
| Caixa (cartão, painel, bloco) | **18px** |
| Pílula (etiqueta, tag, botão) | **999px** |
| Círculo (marcador, avatar, ponto) | **50%** |

**O erro que gerou esta regra:** uma regra de CSS que pretendia unificar raios listou, no mesmo seletor, cartões e etiquetas, e aplicou 999px a todos. Os cinco cartões do método e os três cartões de casos viraram cápsulas. A intenção era boa, a execução misturou duas naturezas diferentes de componente.

**Como não repetir:** antes de aplicar raio a um seletor múltiplo, conferir se todos os elementos da lista são da mesma natureza. Cartão e etiqueta nunca compartilham raio.


---

## O critério final, definido em 4 de agosto de 2026

Quando houver dúvida sobre qualquer alteração futura, a pergunta não é se ela deixa o site mais bonito. A pergunta é esta:

> **O IAieu não explica inteligência artificial. O IAieu reduz complexidade antes que ela se transforme em ansiedade.**

O visitante deve terminar a navegação com menos peso mental do que tinha quando entrou. Alteração que não faz isso não deve ser feita, por melhor que pareça.

A partir desta data o site é **produto em operação**, não projeto em desenvolvimento. Nenhuma alteração deve nascer de opinião estética. As próximas evoluções vêm de casos reais, do comportamento dos visitantes, de dúvidas recorrentes, de novos conteúdos e do amadurecimento natural da marca.
