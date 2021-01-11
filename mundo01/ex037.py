'''Escolha um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão
[1]Converter para binário
[2]Converter para octal
[3]Converter para hexadecimal''')
opção = int(input('escolha: '))

if opção == 1:
    print(f'{num} convertido para binário é: {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print('Opção invalida')