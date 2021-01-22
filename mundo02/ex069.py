'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário que ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados. 
C) Quantas mulheres tem menos de 20 anos.'''

homem = 0
mulher = 0
maiores = 0
sexo = ' '
opcao = ' '
while True:
    print('-' * 20)
    print('Cadastre uma pessoa.')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maiores += 1
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo[M / F]: ')).upper().strip()
        if sexo == 'M':
            homem += 1
        elif idade < 20 and sexo == 'F':
            mulher += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar?[S / N] ')).upper().strip()
    if opcao == 'N':
        break
    sexo = ' '
    opcao = ' '
print(f'Existem {homem} homens;\nExistem {maiores} maiores que 18 anos;\nExistem {mulher} mulheres menores que 20 anos')
