#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestração mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('Insira seus dados analisarmos o seu emprestimo!')
valordacasa = float(input('Qual o valor da casa em questão?:'))
salario = float(input('Qual o seu salário?:'))
quantosanos = float(input('Em quantos anos pretende pagar?:'))

preconoano = valordacasa / quantosanos
prestacaomensal = preconoano / 12
print(f'O valor da prestação mensal será: {prestacaomensal:.2f}')
salarioxprecodacasa = salario * 0.3 # 30% de 4000 é 1200
if salarioxprecodacasa < prestacaomensal:
    print('Infelizmente não podemos aprovar seu emprestimo pois o seu salário é 30% menor do que o valor da prestação da casa')
elif salarioxprecodacasa > prestacaomensal:
    print('Podemos aprovar o emprestimo!')
print('Aguarde o retorno dessas mensagens no seu emai!')

#Ou como foi feito pelo guanabara


print('Insira seus dados analisarmos o seu emprestimo!')
valordacasa = float(input('Qual o valor da casa em questão?:'))
salario = float(input('Qual o seu salário?:'))
quantosanos = float(input('Em quantos anos pretende pagar?:'))
prestacao = valordacasa / (quantosanos * 12)
mínimo = salario * 30 / 100
if prestacao <= mínimo:
    print('Emprestimo pode ser efetuado!')
else:
    print('O emprestimo não pode ser efetuado!')
