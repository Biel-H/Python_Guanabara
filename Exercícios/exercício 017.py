#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = (co **2 + ca **2) ** (1/2)
print(f'a hipotenusa é: {h:4f}')

#ou 
import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(ca, co)
print(f'A hipotenusa é: {h}')