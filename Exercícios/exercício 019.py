#Um professor quer soretear um dos seus quatro alunos para apagar o quadro faça um programa que ajude ele, lendo o nome dele e escrevendo o nome do escolhido
import random
nome = random.choice(['Gabriel', 'Luiz', 'Ana', 'Julia'])
print(f'O escolhido para apagar o quadro foi:{nome}')

#ou
import random
n1 = input('Insira o primeiro nome:')
n2 = input('Insira o segundo nome:')
n3 = input('Insira o terceiro nome:')
n4 = input('Insira o quarto nome:')
r = random.choice([n1, n2, n3, n4])
print(f'O nome escolhido foi:{r}')

#Usando o valor de lista
import random
n1 = input('Insira o primeiro nome:')
n2 = input('Insira o segundo nome:')
n3 = input('Insira o terceiro nome:')
n4 = input('Insira o quarto nome:')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O escolhido foi {escolhido}')


#Com uma pequena automação o ian me fez ajudou a fazer um codigo que lê diversos nomes e escolh entre eles
import random

lista_de_nomes_sus = []
while True:
    sus_da_vez = input('Insira um nome sus (digite: "finalize" para finalizar): ')
    if sus_da_vez != "finalize":
        lista_de_nomes_sus.append(sus_da_vez)
    else:
        break

aluno_escolhido = lista_de_nomes_sus[   random.randint(0, len(lista_de_nomes_sus))   ]

print(f'O aluno escolhido por ser mais sus foi: {aluno_escolhido}')