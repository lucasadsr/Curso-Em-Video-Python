# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

alt = float(input('Qual a altura (metros) da parede? '))
l = float(input('Qual a largura (metros) da parede? '))
area = (alt*l)
litros = (area/2)

print(f'A área da parede é: {area}m², e vai precisar de {litros} litros de tinta.')
