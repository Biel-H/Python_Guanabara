#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento
#Para salários acima de R$1.200,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário?:'))
salarios_altos = 1200 * 10 / 100
total_salario_alto = salario + salarios_altos
salario_baixo = salario * 15 / 100
total_salario_baixo = salario + salario_baixo
if salario > 1200:
    print('O seu salário atual com o aumento de 10% é:',total_salario_alto)
else:
    print(f'O seu salário é de {salario} por isso o aumento é de 15%' '\n' 'O seu salário atual é:',total_salario_baixo)

#ou de forma mais clean

salario = float(input('Qual o seu salário?:'))
if salario < 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo= salario + (salario * 10 / 100 )
print(f'O seu novo salário é: {novo}')