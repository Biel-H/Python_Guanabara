#Faça um programa que leia três números e mostre qual é o maior e qual é o menor
numero1 = int(input('Adicione o 1º número:'))
numero2 = int(input('Adicione o 2º número:'))
numero3 = int(input('Adicione o 3º número:'))

maior = numero1
if (numero2 > maior):
    maior = numero2
if (numero3 > maior):
    maior = numero3
print('O maior é:',maior)
menor = numero1
if (numero2 < menor):
    menor = numero2
if (numero3 < menor):
    menore = numero3
print('O menor é:', menor)