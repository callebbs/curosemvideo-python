'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''

import math

numero = float(input("Digite um número real qualquer: "))

print('O número digitado foi {} e sua porção inteira é {}.'.format(numero, math.trunc(numero)))