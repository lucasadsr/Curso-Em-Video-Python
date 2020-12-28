# Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = input('Qual o nome do aluno 1? ')
aluno2 = input('Qual o nome do aluno 2? ')
aluno3 = input('Qual o nome do aluno 3? ')
aluno4 = input('Qual o nome do aluno 4? ')
nomes = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi:', choice(nomes))
