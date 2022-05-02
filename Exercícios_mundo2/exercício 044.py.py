# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor que será pago?:'))
print("""Lembrando que: 
à vista dinheiro/cheque: 10% de desconto - 1
à vista no cartão: 5% de desconto - 2
em até 2x no cartão: preço normal - 3 
3x ou mais no cartão: 20% de juros - 4 """ )
valoravista = (valor * 10 / 100)
valorcartao = (valor * 5 / 100)
valor3x = (valor * 20  / 100) + valor  
metodopagamento = input('Escolha seu metodo de pagamento, de 1 a 4:')
if metodopagamento == 1:
    print(f'O valor atual pago no dinheiro/crédito fica {valoravista} ')
elif metodopagamento == 2:
    print(f'O valor do pagamento feito à vista é {valorcartao} ')
elif metodopagamento == 3:
    print(f'O valor em até 2x no cartão fica {valor}, mantém o preço normal')
elif metodopagamento == 4:
    print(f'O valor pago em 3x vezes ou mais será de {valorjuros}')
else:
    print('Seila, se vc quiser pagar de outro jeito usando uma panela então se resolve com o gerente')
 


 #### Certo, porem revisar ####