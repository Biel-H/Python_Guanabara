# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
numero = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
n = numero + (11 - 1) * r
for c in range(numero, n , r):
    print(c)
