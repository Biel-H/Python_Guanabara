# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
print('Os números ímapres que são múltiplos de 3 são')
for c in range(1, 501 , 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1 # ou cont += 1
print(f'A soma dos {cont} valores é {s}')