'''
Faça um altoritmo que leia o preço de um produto e mostra seu novo preço, com 5% de desconto.
'''

preco = float((input('Digite o valor do produto: R$')))

print('O novo valor é de R${:.2f}'.format(preco - (preco * 5 / 100)))