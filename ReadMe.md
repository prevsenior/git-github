# Git and GitHub
Nosso curso de git e github TOP alterado

# Importante
1) Verifique se você está no repositorio correto
2) digite: git branch // para ver qual é a branch que você está e quantas branchs tem
3) Digite: git branch -d nome-da-branch // se você quiser deletar uma branch, mas só funciona se ela já estiver sido mesclada
4) no terminal digite: git status // isso vai te mostrar se tem algo para receber commit.
5) no terminal digite: git add . // vai mandar o arquivo para fase de stage
6) no terminal digite: got commit -m "texto sobre o que está fazendo"
7) no terminal digite: git push origin /nome da branch/

# Dia 01
Aprendemos neste dia sobre GIT, desde como criar um repositorio local até merge de branch
Os passos são:
1) crie ou altere um arquivo
2) no terminal digite: git status // isso vai te mostrar se tem algo para receber commit.
3) no terminal digite: git add . // vai mandar o arquivo para fase de stage
4) no terminal digite: got commit -m "texto sobre o que está fazendo"
5) no terminal digite: git push origin /nome da branch/
Aí o código será enviado para o git hub
6) git checkout -b /nome da branch // você criar a branch a partir da branch main.

Outros comando importantes
- para trocar de Branch você digite: git checkout /nome da branch

O processo total é
1) Aviso: nós não trabalhamos na Branch principal, logo precisamos criar outra branch local.
2) git checkout -b /nome da branch // você criar a branch a partir da branch main.
3) para ver se criou digite: git branch
4) para mudar para a branch que você criou digite: git checkout /nome da branch

O ciclo é:
1) Faça um clone da branch main considerando o repositório que você quer no github. Para isso você pode:
Vá para uma pasta onde você vai criar a pasta automaticamente que tem no git
Abra o GitBash e digite: git clone /link do repositório no git
2) vamos clonar a branch main em outra branch digite: git chechout -b /nome da branch
Isso vai clonar tudo que tem na branch main para a nova branch. Vamos alterar lá.
3) Apos concluido a alteração vamos:
31) git add . //para adicionar as alteracoes em stage
32) git commit -m "mensagem" // para fazer o commit
33) git push origin /nome branch // para enviar isso ao repositorio.




