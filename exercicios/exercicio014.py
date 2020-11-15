'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''

temp = float(input('Qual é a temperatura atual? '))

print('A temperatura de {}°C convertida para Farenheit é de: {}°F'.format(temp, (temp * 9/5) + 32))