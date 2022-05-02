# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - para  binário
# - para octal
# - para hexadecimal
numint = int(input('Escreva um número inteiro:'))
binario = bin(numint)
hexadecimal = hex(numint)
octal = oct(numint)
print('Coloque 1 = Binario' '\n' 'Coloque 2 = octal' '\n' 'Coloque 3 = hexadecimal')
opcao = int(input('Coloque um número de 1 a 3:'))
if opcao == 1:
    print(binario)
elif opcao == 2:
    print(octal)
elif opcao == 3:
    print(hexadecimal)
else:
    print('Você não adicionou um número valido')
print('Boa!! os seus números convertidos ficaram desse jeito')
