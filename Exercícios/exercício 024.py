#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com apalavra "Santo"
nome = str(input('Qual o nome da sua cidade?:')).strip()
print(nome[:5].upper() == 'SANTO')

