#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
    psd = float(input('Coloque o preço do seu produto = R$'))
    pcd = psd / 0.05
    print(f'O desconto será de 5%, o preço atual dele será: {pcd:.1f}')
