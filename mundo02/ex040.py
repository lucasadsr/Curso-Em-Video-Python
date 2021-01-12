'''Crie um programa que leia duas notas de um aluno e calculesua média, mostrando uma mensagemno final, de acordo com sua média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7,0 ou superior: APROVADO'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif media <= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
