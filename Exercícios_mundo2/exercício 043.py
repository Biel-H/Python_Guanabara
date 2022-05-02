# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

altura = float(input('Qual é a sua altura?'))
peso = float(input('Qual é o seu peso?'))
imc = peso / (altura * altura)
print(f'Seu imc é {imc:.2f}')
if imc <= 18.5:
    print('Você esta abaixo do peso.')
elif imc > 18.5 and imc <= 25:
        print('Você esta no peso ideal!')
elif imc > 25 and imc <= 30:
    print('Cuidado você esta com sobrepeso.')
elif  imc > 30 and imc <= 40:
    print('Você pode estar com obesidade, vá a um médico!')
else:
    print('Você esta com obesidade mórbida, boa sorte!')

