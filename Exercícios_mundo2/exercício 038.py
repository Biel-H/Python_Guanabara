#Escreva um programa que leia dois números e compare-os mostrando na tela uma mensagem
# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# - não existe valor maior, os dois são iguais

print('Adicione dois números para ser feita uma comparação.')
numero1 = int(input('Coloque o primeiro número:'))
numero2 = int(input('Coloque o segundo número:'))

if numero1 > numero2:
    print(f'O número {numero1} é maior')
elif numero1 < numero2:
    print(f'O número {numero2} é maior')
elif numero1 == numero2:
    print('Ambos os números são iguais!')
else:
    print('Adicione um valor inteiro!!')