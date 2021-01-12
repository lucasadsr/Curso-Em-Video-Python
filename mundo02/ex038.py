'''Escreva um programa que leia dois números inteiros e compare-os, comstrandona tela a seguinte mensagem:
-O primerio valor é maior
-O segundo valor é mior
-Não existe maior valor, os dois são iguais'''

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior que o segundo')
elif num2 > num1:
    print('O segundo valor é maior que o primeiro')
else:
    print('Não existe maior valor, os dois são iguais')