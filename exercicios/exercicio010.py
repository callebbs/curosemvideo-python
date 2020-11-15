'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

Considere:
1 Dólar = R$3,27
'''

valor = float(input("Digite o valor em reais para a conversão em dólar: R$"))
dolar = 3.27
conv = valor * dolar

print("R${} em dólar é de {:.2f}".format(valor, conv))