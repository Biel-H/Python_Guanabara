#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
print('Vamos analisar o seu nome!')
nome=str(input('Insira seu nome completo:')).strip()
nomeseparado = nome.split()
print('O seu primeiro nome é:', nomeseparado[0])
print('O seu último nome é:', nomeseparado[-1])
