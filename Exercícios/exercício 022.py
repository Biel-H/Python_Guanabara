#Crie um programa que leia o nome completo de uma pessoa e mostre:
    #> O nome com todas as letras maiúsculas
    #> O nome com todas as minúsculas
    #> Quantas letras ao todo (sem considerar espaços)
    #> Quantas letras tem o primeiro nome

print('Insira seus dados abaixo para a conversão')
nome = str(input('Digite seu nome:'))
ma = nome.upper()
mi = nome.lower()
qnt =  len(nome.replace(" ", ""))
qntdt = nome.split()
qntdtt = len(qntdt[0])
compr = len(nome.split()[0])
print(f"""O seu nome completamente em maiúsculo é: {ma}
    agora em minúsculo: {mi}
    A quantidade de letras no seu nome é: {qnt}
    Já a quantidade de letras no seu primeiro nome é:{compr}""" )

    #Ou

nome = str(input('Difite seu nome completo: ')).strip()
print('Analisando seu nome...')
mai = nome.upper()
print(f'Seu no0me em maiúsculos é: {mai}')
min = nome.lower()
print(f'Seu no0me em maiúsculos é: {min}')
maxl = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {maxl} letras')
prmn = nome.find(' ')
print(f'Seu primeiro nome tem: {prmn}')