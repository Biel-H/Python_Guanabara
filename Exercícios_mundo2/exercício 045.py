# Crie um programa que faça o computador jogar Jokenpô com você.
from msilib.schema import tables
import random
from time import sleep
print(40 * '=~')
print('Vamos jogar jokempô!')
print(40 * '=~')
print(""" Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada?""")
# pedra = 0
# papel = 1
# tesoura = 2
jogador = int(input('Digite um número de 1 a 3 para começarmos o jogo:'))
computador = random.randint(0 , 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
if jogador == computador:
    print(f'O computador jogou {computador}')
    print('Droga, Empatamos!')
elif jogador == 0 and computador == 1:
    print('O computador jogou PAPEL ')
    print('O computador ganhou!')
elif jogador == 1 and computador == 2:
    print('O computador jogou TESOURA ')
    print('O computador ganhou!')
elif jogador == 1 and computador == 0:
    print('O computador jogou PEDRA ')
    print('Você ganhou!')
elif jogador == 2 and computador == 1:
    print('O computador jogou PAPEL ')
    print('Você ganhou!')
elif jogador == 0 and computador == 2:
    print('O computador jogou TESOURA')
    print('Você ganhou!')
elif jogador == 2 and computador == 0:
    print('O computador jogou PEDRA')
    print('O computador ganhou!')
else:
    print('Numero invalido, Jogue outra vez.')


# Pode ser usado os valores de "Itens" como uma forma do python motrar a palavra:
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0 , 2)
print(f'O computador escolheu {itens[computador]}')
#Assim ira mostrar automaticamente o que ele escolheu (pedra, papel ou tesoura)
