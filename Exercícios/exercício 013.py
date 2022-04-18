# Faça um algoritimo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento
    sal = float(input('Coloque o valor do salário do funcionario: R$'))
    reaj = sal + (sal * 15/100)
    print(f'O novo salário do funcionário após o reajuste é: R$ {reaj}')

    #ou 

    sal = float(input('Coloque o valor do salário do funcionario: R$'))
    reaj = sal * 0.15
    salt = sal + reaj
    print(f'O novo salário do funcionário após o reajuste é: R$ {salt}')