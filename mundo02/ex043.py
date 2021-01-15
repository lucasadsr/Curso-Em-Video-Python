'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso normal
-25 até 30: Sobrepeso
-20 até 40: Obesidade
-Acima de 40: Obesidade mórbida'''

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura**2)
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal')
elif 25 <= imc <30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('Você Você está em obesidade')
else:
    print('Você está com obesidade mórbida')