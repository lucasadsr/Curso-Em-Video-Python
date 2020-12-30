'''
Faça um programa que leia uma frase pelo teclado e mostre:
→ Quantas vezes aparece a vogal A.
→ Em que posição ela aparece pela primeira vez.
→ Em que posição ela aparece pela última vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A')
frasefind = int(frase.find('A'))
fraserfind = int(frase.rfind('A'))

print(f'Analisando a frase consegui perceber que existe(m) {a} vogal(ais) a;')
print(f'Ela foi encontrada primeiramente no caracter {frasefind + 1};')
print(f'Sua última posição foi no caracter {fraserfind + 1}')
