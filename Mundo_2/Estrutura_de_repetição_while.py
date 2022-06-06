#Estrutura de repetição while
#Vamos supor que você deseja pegar uma maçã mas não sabe quantos blocos percorrer, para isso se usa um estrutura de repetição "Enquanto" (while)
#Dessa forma ficaria:

# enquanto não há maçã:
#    passo
# pega

# Em python ficaria:

while not apple:
    passo
pega

# Outro exemplo seria:
while not apple:
    if bloco:
        passo
    if vazio:
        pula
    if moeda:
        pega
pega

# Ou seja, com esse código se nós tivermos um caminho até uma maçã eles seria: Enquanto não há maçã e possui um bloco ande, se tiver um buraco pule
# Se tiver uma moeda pegue e por fim se há uma maçã pegue.

### Exemplos ###
#imaginemos uma situação de conta:
c =1
while c < 10:
    print(c , '-' ' Ainda não acabou')
    c = c + 1
print('fim')

#Neste código ele ira mostrar todo número de 1 até 10 (enquanto o resultado do número não for 10) e junto desse número ira informar que não acabou

# Vamos supor que há uma sequencia de números que se repetem de forma que você saiba a quantidade, dessa forma:
for c in range (1, 5):
    n = int(input('Digite um valor: '))
print('Fim')

#Agora vamos trocar esse código e fazer de uma forma que sempre que um número diferente de 0 seja selecionado ele repita:
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# Agora trabalhando com hipoteses mais realistas vamos utilizar uma interação com a pessoa:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('Fim')

# Toda vez que um número for colocado ele perguntara se deseja continuar ou não








