# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado. peça a digitação novamente até ter um valor correto
r = 'S'
print('Digite o seu sexo abaixo mas lembre-se de colocar apenas [M/F]')
while r == 'S':
    sexo = str(input('Digite aqui o seu sexo: ')).upper()
    if sexo == 'M':
        print('O valor colocado é válido!')
    elif sexo == 'F':
        print('O valor é válido!')
    elif sexo != 'M' and sexo != 'F':
        print('Valor invalido, digite novamente!')
        str(input('Digite o valor novamente: ')).upper()
        
    r = str(input('Quer continuar [S/N]')).upper()
print('Obrigado por contribuir com nossa pesquisa!')

