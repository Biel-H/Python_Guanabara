# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade 
# - Se ele ainda vai se alistar ao serviço militar 
# - Se é a hora exata de se alistar 
# - Se já passou do tempo do alistamento 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
print('Neste programa você devera informar seu ano de nascimento para informar-mos a você se devera ou não se alistar.')
from datetime import date
Anodenascimento = int(input('Digite seu ano de nascimento:'))
anoatual = date.today().year
idade = anoatual - Anodenascimento
print(f'Você tem {idade} anos certo?')
if anoatual - Anodenascimento == 18:
    print('Você deverar se alistar esse ano')
elif anoatual - Anodenascimento > 18:
    print('Você já deveria ter se alistado')
elif anoatual - Anodenascimento < 18:
    print('Você ainda não pode se alistar!')

