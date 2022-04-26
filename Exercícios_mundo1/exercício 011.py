# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade  de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma areá de 2m²
    A = float(input('Adicione um valor de Altura:'))
    L = float(input('Adicione um valor de Largura:'))
    vc = A * L
    qt = vc / 2
    print(f'O seu ambiente possui {vc}M² de área')
    print(f'Agora teremos que saber a quantidade de tinta necessaria pra sua parede \n considerando o valor {vc}M² a quantidade de tinta será: {qt}L')
