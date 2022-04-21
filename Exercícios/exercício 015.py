#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado
dias = int(input('Quantos dias o carro foi alugado?:'))
Km = float(input('Quantos Km foi rodado?:'))
preco = dia * 60
precokm = km * 0.15
precot = preco + precokm
print(f'O preço total a pagar:{precot}')

#Ou

dias = int(input('Quantos dias o carro foi alugado?:'))
km = float(input('Quantos Km foi rodado?:'))
preco = (dias * 60) + (km * 0.15)
print(f'O preço total a pagar:{preco}')



quantos dias alugados
quantos km rodadados
e total a pagar