#Condições aninhadas
#Basicamente isso é pegarmos estruturas condicionais e colocar dentro de outras estruturas condicionais
#Começamos usando o comando que diz "Senão se" e serve para colocarmos condições dentro da outra:
if carro.equerda():
    carro.siga()
    carro..direita()
    carro.pare()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.pare()
else:
    carro.siga()

#É importante lembrar que podemos sempre colocar Vários "elifs" dentro de um "if" mas só podemos usar o else ou uma vez ou nenhuma
#Também não se pode usar "elif" sem "if"
#Um exemplod de uma condição aninhada (É chamada assim pois esta aninhada uma dentro da outra) pode ser:
nome = input('Qual é o seu nome?')
if nome == 'Gabriel':
    print(f'Seu nome é muito charmoso {}!')
elif nome == 'Paulo':
    print('Nossa que legal meu pai também tem esse nome!')
elif nome == 'Paula': #'In' pode ser usado em vez de igual
    print('Uau!!' '\n' 'A minha mãe também tem esse nome!')
else:
    print('É um nome comum.')
print(f'Bom dia, {nome}!')

#Pode usar outras funções também
nome = input('Qual é o seu nome?')
if nome == 'Gabriel':
    print(f'Seu nome é muito charmoso {}!')
elif nome in 'Paulo Felipe Abraao Anderson': #'In' pode ser usado em vez de igual
    print('É um nome masculino comum!')
else:
    print('É um nome comum.')
print(f'Bom dia, {nome}')