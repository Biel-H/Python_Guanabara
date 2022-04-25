#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
print('=' * 40)
print('Estou pensando em um número de 1 a 5, tente advinhar...') #Apresentação do desafio
print('=' * 40)
import random
adv = int(input('Digite o número que acha que estou pensando:')) #Jogador tenta advinhar o número
num = random.randint(1, 5) #Randomização de um número 
if adv == num:
    print('Você acertou!')
else:
    print('Você perdeu!')
print(f'O número que pensei foi: {num}')

#Posso acrescentar uma biblioteca chamada time e dar uma "Tensão" no resultado do programa
from time import sleep
sleep(3) #para fazer o computador esperar uma quantidade específica de tempo
