#Faça um programa que leio um número de 0 a 9999 e mostra na tela cada um dos digitos separados
num = int(input('DIgite um número de 0 a 9999:'))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f""" Analisando o numero...
A sua Unidade é: {u}
Dezena: {d}
Centena {c}
Milhar {m}""")
