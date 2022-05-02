#Imagine que uma pessoa tem que andar alguns passos até pegar uma laranja, uma forma de fazer isso seria fazer um comando a cada passo dado, porém
# isso demandaria muitos comandos, uma forma mais facil de fazer isso sera usando estruturas de repetição como: for
# Assim ele ira repetir para sempre os comandos de "Passo", e para delimitar um limite e ele não acabar passando da laranja nós utilizaremos:

# Laços de repetição
# Laços de repetição ou interação, são basicamente os limitadores de um looping, por exemplo


laço c intervalo(1 , 10)
    Passo    
pega
# em python ficaria mais ou menos assim:
for c in range(1, 10):
    passo
pega

# Também é possivel adicionar um "if" dentro do for
for c in range(1 ,10):
    if moeda:
        pega
    passo
    pula
passo
pega

# Vamos aos exemplos na prática:
# Vamos imaginar que eu desejo printar a palavara "Oi" 6 vezes, mas em vez de fazer isso 6 vezes eu posso usar um "For" para que repita automático pra mim
for c in range(1 ,6):
    print('Oi')
print('Fim')

# Se caso colocarmos apenas o "c" dentro do print iremos printar os números dentro do range
for c in range(1, 6):
    print(c)
print('FIM!')

# Ira aparecer os números de 1 a 5 no resultado pois o 6 não conta

# Agora se quisermos contar de forma decrescente devemos por o -1 para a interação:
for c in range(0 , 7, -1):
    print(c)
print('FIM!')

# Contar de 0 até 6 pulando de 2 em 2
for c in range(0, 6, 2):
    print(c)
print('FIM!')

# Fazendo ele de uma forma aútomatica onde ele vai até o número que você epecíficar:
n = int(input('Digite um número: '))
for c in range(0, n): # Ou n+1 para aparecer o número completo
    print(c)
print('FIM!')

# Podemos usar por exemplo ele com um valor de estrutura de repetição:
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n # ou s += n
print(f'O somatório de todos valores foi {s}')

# Assim ele irá fazer uma soma de todos os valores que foram repetidos dentro do range
