'''Desenvolva um progaram que leia o nome, idade e sexo de 4 pessoas. No final do peograma, mostre:
-A média de idade do grupo;
-Qual é o nome do homem mais velho;
-Quantas mulheres tem menos de 20 anos.'''

mulheresmenores = 0
nomeoldman = ''
maioridade = 0
idade = 0
somaidade = 0
qtdpessoas = int(input('Quantas pessoas serâo cadastradas? '))

for p in range(1, qtdpessoas + 1):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = int(input('''Digite seu sexo
[ 1 ]HOMEM
[ 2 ]MULHER
'''))
    somaidade = somaidade + idade
    if idade > maioridade and sexo == 1:
        nomeoldman = nome
    if idade < 20 and sexo == 2:
        mulheresmenores += 1

media = somaidade / qtdpessoas
print(f'A média das idades é de {media}.')
print(f'O homem mais velho é: {nomeoldman}')
print(f'Exitem {mulheresmenores} mulheres menores que 20 anos de idade.')
