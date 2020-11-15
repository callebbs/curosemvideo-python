'''
Faça um algoritmo que leia o salário de um funcionário e mostra seu novo salário, com 15% de aumento.
'''

salario = float(input('Digite seu salário: R$'))

print('Seu salário de {:.2f} com aumento de 15% será de: R${:.2f}'.format(salario, salario * 1.15))