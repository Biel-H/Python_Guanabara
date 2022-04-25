
,#Manipulando cadeias de texto
#Site com informações sobre: https://algoritmosempython.com.br/cursos/programacao-python/strings/
#Outro chat que também explica o uso dos formatos de manipulação e trasnformação de string: https://pt.stackoverflow.com/questions/296286/encontrar-determinado-texto-em-uma-string
    #Uma cadeia de carácteres é uma string
    #Toda frase no pyhthon é armazenada em memória, e nessas memórias tem micromemórias que guardam em números cada frase
    #por exemplo, vamos pegar uma frase
    Curso em Video Python
    #Essa frase possui 21 caracteres contando com os espaços e começando do zero
    #Se eu colocar o comando:
    frase[9]
    #Eu vou buscar a 9ª caractere dessa frase (Que no caso é o "V")
    #Agora outro exemplo é:
    frase [9:13]
    #Onde eu vou buscar todos os número de 9 a 13 (o 13º não ira aparecer, pois ele para de contar no 13)
    #Posso fazer uma busca pulando uma quantidade específica de números (No caso nesse exemplo eu estou pulando de 2 em 2)
    frase [9:21:2]
    #Outra importante ideia é:
    frase[9::3]
    #Basiamente ele pegou o 9º até o final, e vai fazer isso pulando de 3 em 3

#Análise de string
    #O primeiro comando usado é o: (len -> lenth - comprimento)
    len(frase)

    #Outra forma de análisar a string é o count, ele vai contar neste exemplo quantas vezes aparecem a letra 'o'
    frase.count('o')
    
    #também posso expecificar a quantidade de espaços que ele pode procurar
    frase.count('o',0, 13)
    # Ele procura a letra 'o' entre espaço 0 e o 13 (lembrando que o 13º nõa aparece)

    #Outra funcionalidade de análise de string é o:
    frase.find('deo')
    #Ele vai dizer quantas vezes ele encontrou "deo"
    #Se o python retornar o valor -1 na frase significa que não existe a palavra da busca

    #Esse operador server também para procurar uma palavra na frase
    'curso' in frase

#Transformando strings
    #Podemos substituir algo na frase
    frase.replace('Python','Android')
    #Antes da virgula a palavra que ele tem que procurar, e depois a palavra que ele usara para substituir

    #Podemos deixar tudo em maiúsculo (exeto o que já estava)
    frase.upper()
    #Da mesma forma que podemos deixar tudo minúsculo
    frase.lower()

    #O comando capitalize pega todas as letras da frase e deixa minúscula enquanto apenas a primeira letra da string fica maiúscula
    frase.capitalize()

    #Já o title tranforma todos os começos de palavras em maiúsculo
    frase.title()

    #Podemos remover todos os espaços "inúteis" na string (Geralmente no começo e no final da str)
    frase.strip()

    #Da mesma forma podemos eliminar apenas os espaços da direita
    frase.rstrip()

    #E podemos remover o espaço da esquerda
    frase.lstrip()

#Funcionalidades de divisão de strings
    #Podemos "Dividir" a frase, onde os espaços serão divididos e tranformados em frases diferentes. Assim cada palavra tem uma numeração única e todas são juntas em espaços maiores com numerações diferentes
    frase.split()

#Funcionalidade de junção de strings
    #Podemos juntar uma string substituindo os espaços por caracteres, aqui cada espaço será substituido por um '-'
    '-'.join(frase)

#Texto completo
    #Caso queremos escrever um texto grande podemos usar aspas três vezes, ex:
    print("""Bem vindos ao curso de python! 
    e as minhas anotações pessoais do curso 
    esse é um exemplo de texto quande que eu posso colocar em apenas um print""")

