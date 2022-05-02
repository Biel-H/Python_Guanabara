#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('Adicione os valores das notas para ser calculado a média')
notaum = float(input('Coloque o valor da primeira nota:'))
notadois = float(input('Coloque o valor da segunda nota:'))
media = (notaum + notadois) / 2
print(f'A média foi: {media}')
if media < 5.0:
    print('Média abaixo de 5.0, você foi reprovado!')
elif media >= 5.0 and media  < 6.9:
    print('Você ficou na média, precisa ir para a recuperação!')
elif media >= 7.0 and media <= 10.0:
    print('Parabens! você foi aprovado')
else:
    print('Você colocou valores de notas inexistentes!!!!!')

