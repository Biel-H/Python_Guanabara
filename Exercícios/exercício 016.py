#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex: 
# Digite um numero: 6.127
#O número 6.0127 tem a parte inteira 6.

from math import trunc
nreal = float(input('Digite um número:'))
pinteira = trunc(nreal)
print(f'O número {nreal} tem a parte inteira {pinteira}')

#ou para fazer de forma completa

import math
nreal = float(input('Digite um número:'))
pinteira = math.trunc(nreal)
print(f'O número {nreal} tem a parte inteira {math.trunc(nreal)}')

#também da para ser usado 
int()nreal 
# e será´transformado em inteiro também

