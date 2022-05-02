# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
for c in range(0, 6):
    par = int(input('Digite um número: '))
    if  par % 2 == 0:
     s = s + par
print(s)
