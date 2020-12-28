# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = input('Qual o nome do aluno 1? ')
aluno2 = input('Qual o nome do aluno 2? ')
aluno3 = input('Qual o nome do aluno 3? ')
aluno4 = input('Qual o nome do aluno 4? ')
nomes = [aluno1, aluno2, aluno3, aluno4]
shuffle(nomes)
print('A ordem de apresentação é:')
print(nomes)
