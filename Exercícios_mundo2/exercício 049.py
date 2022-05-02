# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilzando um laõ for.
print('=-' * 40)
print('''Vamos calcular a tabuada!!
 Insira a baixo o número que deseja ver tabuada.''')
print('=-' * 40)
numero = int(input('Digite o número:'))
for c in range (0 , 11):
    print(f'{numero} x {c} = {numero * c}')
