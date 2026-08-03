# NEXT

## Missão

Construir um sistema de trabalho com IA que funcione mesmo quando eu esquecer onde parei.

## Onde parei

A separação física entre site e negócio foi concluída em 2 de agosto de 2026. Não há etapa em andamento.

O site agora vive sozinho em `/Users/cae/IAieu-site`, que é o ambiente oficial e o único repositório Git. A pasta `/Users/cae/iaieu` ficou só com o negócio e não tem mais Git, então não é mais capaz de publicar nada por engano.

Existem duas redes de segurança, e nenhuma delas é para trabalhar: a quarentena em `/Users/cae/IAieu-quarentena-site-2026-08-02`, com a cópia antiga do site e do Git, e o backup em `/Users/cae/Backup-IAieu-2026-08-02`, com tudo como estava antes.

O trabalho do site vive em `imagens/`, `dados/` e `docs-geo/`. O `.gitignore` foi blindado: por padrão ele bloqueia tudo, e só passa o que está na lista de permissão. Arquivo novo do site precisa ser liberado de propósito.

O site está publicado no commit `9abaa2d` e foi conferido página por página, no ar. Depois da separação, os 440 arquivos foram conferidos por hash e os testes do projeto passaram com 231 aprovações e nenhuma falha.

Decisões conscientes, para não serem desfeitas sem querer: `logo_horizontal.png` e `og-image.png` ficam na raiz, porque são endereços já divulgados.

Uma pendência conhecida: o `admin.html` tem 14 travessões, o que reprova na regra da casa. Já era assim antes da reorganização e não piorou com ela, por isso não é urgente.

Este arquivo e o `docs-geo/HISTORICO-TECNICO.md` foram atualizados depois da última publicação, então ainda não estão no ar. O site não depende deles.

Se você quiser saber **por que** alguma coisa ficou do jeito que ficou, está tudo em `docs-geo/HISTORICO-TECNICO.md`, do mais recente para o mais antigo.

## Próxima ação

Nenhuma. A separação acabou e não há pendência técnica crítica.

Daqui para frente, melhoria só nasce de problema real encontrado no uso. Nada de etapa nova por iniciativa própria.

Quando você quiser, e só quando quiser, resta limpar os 14 travessões do `admin.html`.
