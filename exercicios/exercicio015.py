'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros foram percorridos durante sua viagem? '))

print('-----------\nDias alugados: {} \nQuilômetros percorridos: {}\nPreço a pagar: R${}'.format(dias, km, (dias * 60) + (km * 0.15)))


