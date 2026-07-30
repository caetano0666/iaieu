# Bing Webmaster Tools: instalação e uso

Este arquivo é para quem não é técnico. Cada passo diz onde clicar e o que esperar ver na tela.

Por que fazer isso: o Bing é o buscador da Microsoft. Ele alimenta o Copilot, que é o assistente de IA que vem embutido no Windows, no Word e no Edge. Quando alguém pergunta algo ao Copilot, quem responde por trás usa o índice do Bing. Estar bem no Bing é o caminho mais direto para ser encontrado por assistentes de IA da Microsoft.

Tempo total: cerca de 15 minutos, uma vez só.

Endereço: https://www.bing.com/webmasters

---

## 1. Criar a conta

1. Abra https://www.bing.com/webmasters no navegador.
2. Vai aparecer uma tela de boas-vindas com três botões grandes de login: `Microsoft`, `Google`, `Facebook`.
3. Clique em **`Google`**. Esse é o caminho mais fácil, porque é a mesma conta que já usa o Search Console.
4. Escolha a conta `czamma@gmail.com` na lista que aparece.
5. O Google pergunta se você autoriza o Bing Webmaster Tools a ver seu nome e e-mail. Clique em `Continuar`.
6. Pode aparecer uma tela pedindo para aceitar os termos de uso da Microsoft. Leia e, se concordar, marque a caixinha e clique em `Aceitar`. Você precisa aceitar para usar a ferramenta.
7. Pronto, você está dentro do painel.

---

## 2. Importar a verificação do Google (caminho fácil)

Como o iaieu.com já está verificado no Google Search Console, o Bing consegue puxar tudo de lá sem precisar mexer em arquivo nenhum do site. Use este caminho.

1. Na tela inicial do painel, aparecem duas caixas lado a lado:
   - À esquerda: `Importar sites do GSC`
   - À direita: `Adicionar site manualmente`
2. Clique no botão **`IMPORTAR`** da caixa da esquerda.
3. Abre uma janela do Google pedindo permissão para o Bing acessar os dados do Search Console. Escolha de novo a conta `czamma@gmail.com` e clique em `Continuar`.
4. O Bing mostra a lista das propriedades que existem no seu Search Console. Você deve ver `iaieu.com` na lista.
5. Marque a caixinha ao lado de `iaieu.com`.
6. Clique em `Importar`.
7. Espere. Aparece uma barra de progresso. Ao terminar, uma mensagem verde confirma a importação e o site vai para o painel já verificado.
8. Confirme: no canto superior esquerdo, a caixinha de seleção de site deve mostrar `iaieu.com`. E não deve haver nenhum aviso amarelo de "site não verificado".

Se a importação falhar, existe o plano B manual, mas ele exige colocar um arquivo novo na raiz do site. Nesse caso, peça ajuda técnica e não tente sozinho.

O que a importação já traz de brinde: os sitemaps que estavam no Google vêm junto. Ainda assim, confira na seção 3.

---

## 3. Enviar o sitemap

Sitemap é a lista de endereços do seu site, num arquivo que os buscadores sabem ler. O do IAieu já existe em `https://iaieu.com/sitemap.xml`.

1. No menu da esquerda, clique em `Sitemaps`.
2. Olhe a tabela do meio da tela. Se já aparecer uma linha com `https://iaieu.com/sitemap.xml` e o estado `Êxito` ou `Success`, está feito. Pule para a seção 4.
3. Se a tabela estiver vazia, clique no botão azul `Enviar sitemap`, no canto superior direito.
4. Abre uma caixinha com um campo de texto. Digite ou cole exatamente:

```
https://iaieu.com/sitemap.xml
```

5. Clique em `Enviar`.
6. A linha aparece na tabela. No começo o estado pode ficar `Pendente`. Volte no dia seguinte e confirme que virou `Êxito`. Deve mostrar 7 URLs descobertas, que é o número de páginas listadas hoje no sitemap.

Se o estado ficar `Falha`, abra `https://iaieu.com/sitemap.xml` no navegador. Se a página não abrir, o arquivo sumiu do site e isso é grave, veja `FUTURE-MAINTENANCE.md`.

---

## 4. Onde olhar depois, no dia a dia

| Menu da esquerda | Para que serve |
|---|---|
| `Desempenho da pesquisa` | Cliques, impressões e as palavras que trouxeram gente pelo Bing. Mesma lógica do Search Console |
| `Inspeção de URL` | Cola um endereço e vê se o Bing conhece aquela página |
| `Sitemaps` | Confere se a lista de páginas está sendo lida |
| `Verificação do site` | Confirma que a propriedade continua verificada |
| `IndexNow` | Onde fica a chave explicada na seção 5 |

Sugestão de frequência: uma olhada por mês, junto com a rotina do Search Console.

---

## 5. IndexNow

### O que é, em uma frase

IndexNow é um aviso instantâneo que o site manda para o Bing dizendo "esta página mudou, vem olhar de novo", em vez de esperar o robô passar por conta própria.

### Por que interessa

O Copilot e o Bing usam esse aviso para saber que a página mudou. Sem ele, pode levar dias até o buscador perceber uma alteração. Com ele, o pedido de releitura entra na fila em segundos. Não é garantia de indexação rápida, é só um aviso, mas é um aviso que custa nada.

### Como a chave funciona

A chave é um código aleatório, uma sequência de letras e números. Ela precisa existir em dois lugares ao mesmo tempo:

1. Dentro do endereço que você chama para avisar.
2. Num arquivo de texto simples na raiz do site, com o nome sendo a própria chave mais `.txt`, e o conteúdo do arquivo sendo a própria chave.

Exemplo: se a chave for `abc123`, o arquivo se chama `abc123.txt`, fica em `https://iaieu.com/abc123.txt`, e ao abrir esse endereço no navegador você deve ver escrito na tela apenas `abc123`.

É assim que o Bing confirma que quem mandou o aviso é mesmo o dono do site.

### Passo a passo para gerar a chave

1. No painel do Bing Webmaster Tools, menu da esquerda, clique em `IndexNow`.
2. Clique em `Gerar chave` ou `Generate key`.
3. O Bing mostra na tela um código longo. Copie esse código inteiro.
4. Ainda nessa tela, o Bing oferece um link para baixar o arquivo `.txt` já pronto. Baixe.
5. Esse arquivo precisa ser colocado na raiz do site iaieu.com, ou seja, no mesmo lugar onde estão `index.html` e `sitemap.xml`. Isso é uma tarefa técnica, peça a quem publica o site. Não tente fazer pela interface do Bing, ele não publica nada no seu site.
6. Depois de publicado, abra no navegador `https://iaieu.com/SUACHAVE.txt` trocando `SUACHAVE` pelo código. Você tem que ver o código escrito na tela. Se der erro 404, o arquivo não foi para o lugar certo.
7. Volte no painel do Bing, na tela do IndexNow, e clique em `Verificar` ou `Verify`. Deve aparecer confirmação verde.
8. Anote a chave num lugar seguro. Ela não é secreta, mas se perder é chato de recuperar.

### Comando de ping pronto

Depois que a chave estiver publicada, este é o comando que avisa o Bing de que uma página mudou. Ele é digitado no aplicativo Terminal do Mac.

```
curl "https://api.indexnow.org/indexnow?url=https://iaieu.com/&key=CHAVE&keyLocation=https://iaieu.com/CHAVE.txt"
```

Como usar:

1. Copie a linha acima.
2. Troque **as duas ocorrências** da palavra `CHAVE` pela chave real que o Bing gerou. As duas, tanto a que vem depois de `key=` quanto a que aparece no nome do arquivo em `keyLocation=`. Se trocar só uma, não funciona.
3. Se a página que mudou não for a home, troque também `https://iaieu.com/` logo depois de `url=` pelo endereço da página. Exemplo para a página de conteúdos:

```
curl "https://api.indexnow.org/indexnow?url=https://iaieu.com/conteudos.html&key=CHAVE&keyLocation=https://iaieu.com/CHAVE.txt"
```

4. Abra o aplicativo `Terminal` no Mac, cole a linha e aperte Enter.
5. O que esperar: o comando não responde nada, ou responde bem pouco, e volta para a linha de comando. Silêncio aqui é sinal de sucesso. Se aparecer uma mensagem de erro com um número tipo `422` ou `403`, provavelmente a chave está errada ou o arquivo `.txt` não está no ar.

### Observação sobre a chave já presente no site

Existe hoje na raiz do site um arquivo de chave IndexNow chamado `24e8019110bddcf5ce9d83b015ca44ca.txt`, cujo conteúdo é a própria chave `24e8019110bddcf5ce9d83b015ca44ca`. Se essa é a chave em uso, o comando fica assim, já pronto:

```
curl "https://api.indexnow.org/indexnow?url=https://iaieu.com/&key=24e8019110bddcf5ce9d83b015ca44ca&keyLocation=https://iaieu.com/24e8019110bddcf5ce9d83b015ca44ca.txt"
```

Antes de confiar nesse comando, faça duas conferências:

1. Abra `https://iaieu.com/24e8019110bddcf5ce9d83b015ca44ca.txt` no navegador. Tem que aparecer a chave escrita na tela.
2. No painel do Bing, tela `IndexNow`, confirme que essa é a chave reconhecida. Se o painel mostrar outra chave, use a do painel e refaça a seção anterior.

Esse arquivo `.txt` entra na lista de arquivos que nunca podem ser apagados. Veja `FUTURE-MAINTENANCE.md`.

### Quando disparar o ping

- Publicou página nova.
- Reescreveu o texto principal de uma página.
- Corrigiu um erro visível numa página.

Não dispare para toda alteração mínima. Mandar aviso demais sem mudança real faz o Bing passar a ignorar seus avisos.

---

## 6. Lembretes

- Ninguém garante posição no Bing nem citação garantida em nenhum assistente de IA. IndexNow acelera o aviso, não compra resultado.
- O arquivo da chave `.txt` na raiz do site entra na mesma lista de arquivos que nunca podem ser apagados. Veja `FUTURE-MAINTENANCE.md`.
- Nunca mexa no arquivo `google7279386773b5d258.html`. Ele é do Google e não tem relação com o Bing.
