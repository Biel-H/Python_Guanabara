#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Digite seu nome completo:'))
print(f'Seu nome tem Silva?:', 'silva' in nome.lower())

#ou, pode implementar de uma forma que fique em português

nome = input('Digite seu nome:')
ts = 'Sim' if 'Silva' in nome else 'Não'
print(f'Seu nome tem Silva? {ts}', 'silva' in nome.lower())

#Um erro que não consegui resolver foi aparecer como resposta 'Sim' e 'True' no mesmo resultado
