# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
    from cgitb import text
from wsgiref.validate import validator


d = float(input('Adicione um valor ao conversor de moedas:'))
vd = d / 4.79
ve = d / 5.8
print(f'O seu valor comvertido a dolar fica: {vd:.2f} \n  Já o valor convertido em euro fica: {ve:.2f}')
