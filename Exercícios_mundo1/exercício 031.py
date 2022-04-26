#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viajens mais longas

dis = float(input('Qual a distância da viagem?:'))
passagem = dis * 0.50
passagemaior = dis * 0.45
if dis <= 200:
    print(f'O preço da passagem será R${passagem}')
else:
    print(f'O preço da passagem será R${passagemaior}')
    
#Ou de forma simplificada/operador ternario

dis = float(input('Qual a distância da viagem?:'))
preco = dis * 0.50 if dis <=200 else dis * 0.45
print(f'E o preço da sua passagem será de R${preco}')