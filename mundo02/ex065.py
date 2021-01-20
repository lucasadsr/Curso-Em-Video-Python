'''Crie um programa que leiavários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O programa ao usuário se ele quer ou não continuar a digitar os valores.'''

n = int(input('Digite um número inteiro: '))
opcao = str(input('''Deseja continuar?
[ S ]SIM
[ N ]NÃO
''')).upper().strip()
media = maior = menor = soma = n
cont = 1

while opcao == 'S':
    n = int(input('Digite outro número inteiro: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    opcao = str(input('''Deseja continuar?
[ S ]SIM
[ N ]NÃO
''')).upper().strip()
    cont += 1

media = soma / cont
print(f'O maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
print(f'A média dos número digitados é: {media:.2f}')