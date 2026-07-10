# LEIA-ME — Site IAieu

Guia simples, em português, pra você entender e cuidar do seu site.
Você não precisa saber programar. Na dúvida, é só abrir o Claude Code
nesta pasta (`iaieu`) e me pedir o que quiser.

---

## O que é o site

- Endereço: **iaieu.com**
- Fica publicado de graça no **GitHub Pages** (atualiza sozinho quando a gente publica).
- Marca: **IAieu** (sem "Instituto").
- Produto principal: **IAieu eVc** (gestão da sua presença no LinkedIn, na sua voz).
- Também: **IAieu+** (você traz o problema, a gente entrega a solução) e **IAieu GO** (curso de 3 sessões, R$249).

### A estrutura (agora é uma página só)

O site é uma **única página** (`index.html`) por onde você **rola pra baixo**.
O menu no topo leva direto pra cada trecho:

1. **Topo** — a frase de impacto e a palavra "Alívio".
2. **IAieu eVc** — o serviço principal (presença no LinkedIn), em destaque.
3. **IAieu+** — solução sob medida por WhatsApp.
4. **IAieu GO** — o curso, R$249.
5. **Sobre** — origem, trajetória e a crença da marca.
6. **Casos Reais** — Andrea, Bruno e Patty.
7. **Depoimentos** — o que dizem os clientes.
8. **Contato** — o WhatsApp e as redes.

Fora dela existe só mais uma página aberta ao público:

- **Depoimentos** (`depoimentos.html`) — a página com o **formulário** pra cliente deixar depoimento. O botão "Deixe seu depoimento" na página principal leva até ela.

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
- "Troca o texto da seção Sobre por este: ..."
- "Muda o número do WhatsApp pra ..."
- "Coloca uma foto nova no lugar de tal imagem."
- "Tira o depoimento da Fulana."

---

## Detalhes técnicos (só pra referência)

Você não precisa disto no dia a dia. Fica aqui caso outra pessoa vá mexer.

- Site estático (HTML/CSS), sem servidor. Repositório no GitHub: `caetano0666/iaieu`.
- Publicação: `git commit` + `git push` na branch `main` → GitHub Pages.
- Páginas: `index.html` (a página única) e `depoimentos.html` (formulário). `admin.html` é o bastidor pra gerenciar depoimentos.
- Visual compartilhado: `estilo.css`.
- Cores: fundo `#0A0A0F`, roxo `#7C3AED`, azul `#2563EB`, cinza `#A0A0B8`. Fonte: Inter.
- Regra de estilo do texto do site: **sem travessões (—)**.
- Contato principal: WhatsApp **+1 754 252 5245**. Instagram: **@institutoiaieu**.
- Os depoimentos exibidos ficam no arquivo `config.json` (lista "depoimentos").
- Logos: o "IAieu." do menu e do rodapé é **texto** (sempre nítido); o símbolo é `simbolo_t.png`.

---

Qualquer coisa, abra o Claude Code nesta pasta e fale comigo. Eu lembro de tudo. 🙂
