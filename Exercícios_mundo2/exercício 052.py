# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input('Digite um número: '))
cont = 0
for c in range(1 , numero + 1):
    if numero % c == 0:
        cont += 1
        print(c, end=' ')
print(f'Foi a quatidade de números divisíveis por {numero}')
if cont == 2:
    print(f'{numero} é primo.')
else:
    print(f'{numero} não é primo pois é divisível por mais de 3 números')

# Ou


num = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
print(f'O número {numero} foi divisível {total} vezes')
if total == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')