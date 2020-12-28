# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse ângulo.

import math
a = float(input('Qual o valor do ângulo? '))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print(f'O valor do seno é de {seno:.2f}\n'
      f'O valor so cosseno é de {cosseno:.2f}\n'
      f'O valor da tangente é de {tangente:.2f}')
