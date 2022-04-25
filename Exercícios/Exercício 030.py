#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar
num = int(input('Ponha um número inteiro:'))
par = num % 2
if par == 0:
    print('O número é Par!')
else:
    print('O número é ímpar')