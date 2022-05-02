#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
anodenascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - anodenascimento
print(f'Sua idade é {idade}')
if idade <= 9:
    print('Você é um atleta MIRIM!')
elif idade > 10 and idade <= 14:
    print('Você é um atleta INFANTIL!')
elif idade > 14 and idade <= 19:
    print('Você é um atleta JUNIOR!!')
elif idade > 19 and idade <= 25:
    print('Você é um atleta SÊNIOR!')
elif idade >= 25:
    print('Você é um atleta MASTER!')
else:
    print('Acho que esta muito além da ídade, cuidado.')


