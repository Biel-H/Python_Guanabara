#Faça um prgrama que leia uma frase pelo teclado e mostre:
#> Quantas vezes aparece a letra "A"
#> Em que posição ela aparece a primeira vez
#> Em que posição ela aparece pela última vez

frase = input('Digite uma frase para análise:').strip()
ca = frase.count('a'.upper().lower())
print(f'O comprimento da frase é: {len(frase)}')
print(f'A letra "A" aparece: {ca} vezes ')
achar = frase.find('a'.lower().upper())+1 #isso (+1) serve para vermos a posição de forma humana
print(f'A primeira vez que ela aparece é na posição: {achar}')
ultima = frase.rfind('A'.lower().upper())+1
print(f'A úlitma letra "A" apareceu na posição {ultima}')

#pode fazer a conta dos "As" dessa forma também
ca = frase.count('a')
ca2 = frase.count('A')
ca3 = ca + ca2


