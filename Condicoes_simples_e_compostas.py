#Condições simples e compostas
    #Representação estruturada ou identada: É uma forma de se "Escrever" os dados, em forma de comando de cima pra baixo
    #A indentação em python funciona de forma que um comando que esteja grudado ou sem espaço no linha tenha a condição de acontecer sempre. A condição de cima sempre será verdadeira
    #Já os comandos que estão aninhados num comando podem ou não ser executados 
        #O python separa os comandos de verdadeiro e falso em blocos ou seja:
        if carro.esquerda():
            bloco True
        else:
            bloco False
    #Isso é chamado de "Condição", nessa condição sempre será executado ou um ou outro. Nunca os dois
    #Cada bloco pode ser separado por "Fluxos" onde por exemplo a condição True é o fluxo verde e a condição False é o fluxo vermelho
    #Um exemplo disso:
    tempo = int(input('QUantos anos tem seu carro?'))
    if tempo <=3:
        print('Carro novor')
    else:
        print('Carro velhor')
    print('_Fim_')


#Vamos começar com uma estrutura condicional simples
nome = input('Qual seu nome?')
if nome == 'Gabriel':
    print('QUe nome lindo você tem')
print(f'Bom dia! {nome}')

    #Aqui ele sempre mostrará o "Bom dia!" pois ele esta colado na esquerda logo ele sempre ocorrerá, já o que esta concatenado com o if só acontecera em uma ocasião expecifica, se for verdadeira.

#Agora com uma estrutura condicional composta
nome = input('Qual seu nome?')
if nome == 'Gabriel':
    print('QUe nome lindo você tem')
else:
    print(f'Que nomezinho normal {nome}')
print(f'Bom dia! {nome}')

#Outro exemplo simples é:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A média foi: {m}')
if m >=6.0:
    print('Sua nota foi boa!')
else:
    print('Sua nota foi razoável, treine mais!')


