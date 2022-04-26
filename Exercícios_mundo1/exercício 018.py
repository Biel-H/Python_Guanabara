#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
ca = float(input('Comprimento do ângulo:'))
ra = math.radians(ca)
s = math.sin(ra)
c = math.cos(ra)
t = math.tan(ra)
print(f'O seno de {ca} é {s:2f} o cosseno é {c:2f} e a tangente é {t:2f}')

#Ou 

import math
ca = float(input('Digite o ângulo desejado:'))
s = math.sin(math.radians(ca))
c = math.cos(math.radians(ca))
t = math.tan(math.radians(ca))
print(f'O ângulo de {ca} possui o seno {s}')

#porém se eu importar específicamente esses metodos eu não preciso referenciar
from math import sin, cos, tan
ca = float(input('Digite o ângulo desejado:'))
s = sin(radians(ca))
c = cos(radians(ca))
t = tan(radians(ca))
