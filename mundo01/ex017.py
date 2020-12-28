# Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print(f'o valor da hipotenusa é: {hypot(co, ca)}')
