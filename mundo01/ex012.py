# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. 

p = float(input('Qual o preço do produto? '))
d = p*0.05
print(f'{p}, com desconto é: {(p - d):.2f}!')
