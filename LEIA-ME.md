# LEIA-ME — Site do Instituto IAieu

Guia simples, em português, pra você entender e cuidar do seu site.
Você não precisa saber programar. Na dúvida, é só abrir o Claude Code
nesta pasta (`iaieu`) e me pedir o que quiser.

---

## O que é o site

- Endereço: **iaieu.com**
- Fica publicado de graça no **GitHub Pages** (atualiza sozinho quando a gente publica).
- Produto principal: **IAieu+** (você traz o problema, a gente entrega a solução pronta).
- Produto secundário: **IAieu GO** (o curso de 3 sessões, R$249).

### As 5 páginas

1. **Início / IAieu+** — a página principal (`index.html`)
2. **IAieu GO** — a página do curso (`iaieu-go.html`)
3. **Sobre** — origem, fundador e filosofia (`sobre.html`)
4. **Depoimentos** — depoimentos + formulário (`depoimentos.html`)
5. **Contato** — WhatsApp direto (`contato.html`)

Todas têm o menu no topo e o botão verde do WhatsApp flutuando no canto.

---

## Como as mudanças vão pro ar

Você **não mexe em código**. O fluxo é sempre este:

1. Você me fala o que quer (ex: "adiciona um depoimento", "muda tal texto").
2. Eu faço a alteração e **publico** (no jargão: "commit e push").
3. Em **1 a 3 minutos** aparece no iaieu.com.
4. Pra ver na hora, abra o site e aperte **Ctrl + F5** (no celular, puxe a tela pra atualizar).

---

## Depoimentos (como funciona a aprovação)

Ninguém publica nada no site sozinho. **Só entra o que você aprova.**

1. O cliente abre a página de Depoimentos e preenche **nome, profissão e depoimento**.
2. Ele clica em **"Enviar pelo WhatsApp"**.
3. O depoimento chega **no seu WhatsApp**, como uma mensagem começando com
   *"Olá! Quero deixar um depoimento para o IAieu..."*.
   - Ele cai **na conversa da pessoa que enviou** (no contato dela), não num contato separado.
   - Pra achar rápido: use a **busca do WhatsApp** e digite **depoimento**.
4. Se você gostou, me manda aqui o **nome, a profissão e o texto**, e eu publico.

Link pra mandar aos clientes (leva direto ao formulário):

    https://iaieu.com/depoimentos.html#form-wrap

---

## Coisas que você pode me pedir (exemplos)

- "Adiciona um depoimento da Fulana, [profissão], com o texto: ..."
- "Muda o preço do curso pra R$..."
- "Troca o texto da página Sobre por este: ..."
- "Muda o número do WhatsApp pra ..."
- "Coloca uma foto nova no lugar de tal imagem."
- "Tira o depoimento da Fulana."

---

## Cadastros do curso IAieu GO

Na página do IAieu GO tem um formulário de inscrição (nome, e-mail, cidade,
telefone). Esses cadastros vão pra uma **planilha do Google** e você recebe um
**e-mail de aviso** em czamma@gmail.com. (Isso é separado dos depoimentos.)

---

## Detalhes técnicos (só pra referência)

Você não precisa disto no dia a dia. Fica aqui caso outra pessoa vá mexer.

- Site estático (HTML/CSS), sem servidor. Repositório no GitHub: `caetano0666/iaieu`.
- Publicação: `git commit` + `git push` na branch `main` → GitHub Pages.
- Visual compartilhado por todas as páginas: `estilo.css`.
- Cores: fundo `#0A0A0F`, roxo `#7C3AED`, azul `#2563EB`, cinza `#A0A0B8`. Fonte: Inter.
- Regra de estilo do texto do site: **sem travessões (—)**.
- Os depoimentos exibidos ficam no arquivo `config.json` (lista "depoimentos").
- Também dá pra gerenciar depoimentos pela página `admin.html`.
- Logos: o "IAieu." do menu e do rodapé é **texto** (sempre nítido); o logo grande
  fica na página Sobre (`logo_oficial_t.png`); o símbolo é `simbolo_t.png`.

---

Qualquer coisa, abra o Claude Code nesta pasta e fale comigo. Eu lembro de tudo. 🙂
