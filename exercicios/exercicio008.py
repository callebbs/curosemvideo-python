'''
Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.
'''

metros = float(input("Digite um valor em metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"O valor {metros:.1f} metros fica: {centimetros:.1f} centímetros e {milimetros:.1f} milimetros.")