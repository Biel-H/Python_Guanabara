#Utilizando Módulos
#O comando 'Import' é um dos primeiros modulos apresentados, com ele podemos importar informações ou dados(todos os dados/tabelas/informações, se entendeu) de uma biblioteca que será usada no nosso código
    import bebida
# caso eu queira importar métodos específicos de uma biblioteca eu uso o 'From'
    from bebida import coca-cola
#Outro exemplo de biblioteca é a "math", ela serve para extensões matemáticas, algumas das suas funcionalidades
    math
        ceil -> para arredondar para cima, ex 7,5 - 8,0
        floor -> para arredondar para baixo, ex: 7,5 - 7,0
        trunc -> para eliminar todo numero depois da virgula
        pow -> potência
        sqrt -> Raiz
        factorial - Para calcular fatoriais
        ex:
    from math import floor, sqrt

#Parte prática
    #Nesse código eu coloquei para o "MATH" arredondar o valor da raiz para cima usando o "ceil"
    import math
    num = int(input('Digite um número'))
    raiz = math.sqrt(num)
    print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

    #caso eu queira arredondar para baixo 
    import math
    num = int(input('Digite um número'))
    raiz = math.sqrt(num)
    print(f'A raiz de {num} é igual a {math.floor(raiz)}')
    #E se eu não quiser arrendodar nada basta eu tirar o "math."

#Agora usando o comando "from" eu posso especícar valores no meu comando
    from math import sqrt, ceil
    num = int(input('Digite um número:'))
    raiz = sqrt(num)
    print(f'A raiz de {num} é {ceil(raiz)}')

#Um lugar para verificar as bibliotecas que podem ser imoportadas é o site www.python.org usando os docs ou o site do PyPi para criar uma biblioteca ou escolher uma personalizada
# ou podera usar o próprio pycharm utilizando o comando import e depois apertando CTRL + ESPAÇO e verá uma listsa com os comandos disponiveis
    #Usando um import que achei eu consigo gerar um numero aleatório usando a biblioteca "random"
        import random
        num = random.random()
        print(num)

         #ou podera aleatórizar um numero inteiro ou de um valor inserido até outro
         import random
         num = random.randint(1, 30)
         print(num)

#Outro exemplo de biblioteca é a de emoji
    import emoji
    print(emoji.emojize("Salve galerinha :stuck_out_tongue_winking_eye:", language='alias'))

    #Site com as listas dos emojis https://www.webfx.com/tools/emoji-cheat-sheet/
