'''
Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros = int(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"O valor {metros} metros fica: {centimetros} centímetros e {milimetros} milimetros.")