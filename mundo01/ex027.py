'''Faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente'''

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu primeiro nome é {nome.split()[0]} e seu último nome é {nome.split()[-1]}.')
