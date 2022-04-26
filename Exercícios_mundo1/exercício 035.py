#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo 
reta1 = float(input('Coloque o tamanho da 1º reta:'))
reta2 = float(input('Coloque o valor da 2º reta:'))
reta3 = float(input('Coloque o valor da 3º reta:'))

a = reta1
b = reta2
c = reta3

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os valores conferem e a reta pode ser usada pra fechar o triângulo!')
else:
    print('Os valores não poder fechar um triângulo!')

    #Ou

reta1 = float(input('Coloque o tamanho da 1º reta:'))
reta2 = float(input('Coloque o valor da 2º reta:'))
reta3 = float(input('Coloque o valor da 3º reta:'))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
   print('Os valores conferem e a reta pode ser usada pra fechar o triângulo!')
else:
    print('Os valores não poder fechar um triângulo!')
