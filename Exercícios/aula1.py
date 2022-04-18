Primeiros comandos do python

#Primeiros comandos do python
    #O Primeiro comando basico é o 'Print' que basicamente mostra algo na tela
        print('Bem vindo?')
    
    #Agora adicione uma variavel ao print para mostrar um valor, por exemplo:
        nome = input('Qual o seu nome?')
        print(nome)
    
    #Pode ser adicionados mais valores icluindo os numeros também
        nome = input('Qual é o seu nome?')
        idade = input ('Quantos anos você tem?')
        peso = input ('Qual é o seu peso?')
        print('Boas vindas {}!'.format(nome), 'Seu peso é', peso, 'E você tem apenas', idade, 'isso é preocupante')

    #De forma basica da para realizar contas tambem apenas colocando os numeros e o indicativo de soma, divisão, subtração
        7+5
    
    #Tipos primitivos
        #Em python temos 4 principais tipos primitivos, int, float, bool, str
        #int: todos os números inteiros por exemplo: 7, -4, 0
        #float: todos os números reais, por exemplo: 4.5, 0.076, -15.223
        #bool: Valor condicional para representar sim ou não: True e False (sempre maiúsculo)
        #str: texto, por exeplo tudo que possua as ''

    #Vamos fazer uma conta de soma um pouco avançada:

        n1 = int(input('Que número deseja somar?'))
        n1 = int(input('COloque o segundo número?'))
        s = n1 + n2            print(f'A soma é fodase = {s}')   

    #Ou

        print('Seu numero é:', int(input('Número 1:')) + int(input('Número 2: ')))

    #Nesse código eu fiz um programa que lê algo pelo teclado e mostra na tela o tipo primitivo da minha palavra e as informações possiveis sobre tal

        t1 = input('Digite algo:')
        print('O seu tipo primitivo é:', type(t1), t1.isalnum(), t1.isascii(), t1.isdigit(), t1.islower(), t1.isdecimal(), t1.isidentifier(), t1.isnumeric(), t1.isprintable(), t1.isalnum(), t1.isspace(), t1.istitle(), t1.isupper())

#Operações Aritméticas
    # Cada operador (+, -, *, /, etc...) precisa de um operando (Números) antes e depois de cada operador
    #Eles possuem uma ordem de precadência em 1º = (), em 2ª = **, 3ª = *, /, //, %, e em 4ª = +, -.
    #Agora vamos para os exercicíos
    #É possivel colocar os numeros dentro de um print também, no exemplo eu repito o sinal de '=' 20 vezes
        print('='*20)
    
    #Agora vamos adicionar mais operadores para nossas contas
        n1 = int(input('Um valor:'))
        n2 =  int(input('Outro valor:'))
        s = n1 + n2
        m = n1 * n2
        d = n1 / n2
        di = n1 // n2
        e = n1 ** n2
        print(f'A soma vale = {s}', f'A multiplicação é = {m}', f'A divisão dica ={d:.3f}')
        print(f'A divisão inteira fica com o resultado de: {di}', f'E o resultado da potenciação é: {e}')
    
    #É possivel mostrar os dois prints diferentes em uma mesma linha
        
        n1 = int(input('Um valor:'))
        n2 =  int(input('Outro valor:'))
        s = n1 + n2
        m = n1 * n2
        d = n1 / n2
        di = n1 // n2
        e = n1 ** n2
        print(f'A soma vale = {s}', f'A multiplicação é = {m}', f'A divisão dica ={d:.3f}' end=' ')
        print(f'A divisão inteira fica com o resultado de: {di}', f'E o resultado da potenciação é: {e}')

    #Fiz um codigo que lê um numero inteiro e mostra na tela o seu sucessor e antecessor
        n1 =  int(input('Coloque um numero:'))
        print(f'O antecessor do seu número é: {n1 -1}', f'e o sucessor é {n1 +1}')
    
    #Agora um que calcule operações diferentes
        n1 = int(input('Adicione um número:'))
        print (f'O dobro do seu número é: {n1 * 2}', f'agora o triplo seu número é: {n1 * 3}', f'e por último a raiz quadrado {n1 ** 0.5}')

        