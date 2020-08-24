'''
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele.
'''

texto = input("Digite algo: ")
separador = 50 * "-"
print("O tipo primitivo do que foi digitado é: ", type(texto))
print(separador)
print("O O que foi digitado é um alfanumérico? ", texto.isalnum())
print(separador)
print("O que foi digitado pertence ao alfabético? ", texto.isalpha())
print(separador)
print("O que foi digitado pertence ao numérico? ", texto.isnumeric())
print(separador)
print("O que foi digitado é apenas minúsculo? ", texto.islower())
print(separador)
print("O que foi digitado é apenas maiúsculo? ", texto.isupper())
print(separador)
print("O que foi digitado está capitalizada? ", texto.istitle())
print(separador)
print("O que foi digitado é apenas um espaço? ", texto.isspace())
print(separador)