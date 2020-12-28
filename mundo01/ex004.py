# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

algo = input('Digite algo: ')
print(type(algo))
print(f'Só tem espaços? {algo.isspace()} \n'
      f'É um número? {algo.isnumeric()} \n'
      f'É alfabético? {algo.isalpha()} \n'
      f'É alfanumérico? {algo.isalnum()} \n'
      f'É maiúsculo? {algo.isupper()} \n'
      f'É minusculo? {algo.islower()} \n'
      f'É Capitalizado? {algo.istitle()}')
