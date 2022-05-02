#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

reta1 = float(input('Coloque o tamanho da 1º reta:'))
reta2 = float(input('Coloque o valor da 2º reta:'))
reta3 = float(input('Coloque o valor da 3º reta:'))

a = reta1
b = reta2
c = reta3

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('Os valores conferem e a reta pode ser usada pra fechar o triângulo!')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSELES')
else:
    print('Os valores não poder fechar um triângulo!')
