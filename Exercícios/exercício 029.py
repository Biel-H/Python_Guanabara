#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite

vc = float(input('Qual foi a velocidade do carro?:'))
calm = (vc - 80) * 7
if vc > 80:
    print(f'Você passou do limite de velocidade, a multa cobrada foi {calm}')
else:
    print('Você estava no limite de velociade, Parabens!')
print('Obrigado, volte sempre!')

#caso for feito de forma simples
vc = float(input('Qual foi a velocidade do carro?:'))
calm = (vc - 80) * 7
if vc > 80:
    print(f'Voce passou do limite de velocidade, a multa foi {calm}')
print('Você passou! dirija com segurança!')