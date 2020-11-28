'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input("Digite o nome de uma pessoa: ")).strip()
print("Analisando o nome...")
print("O nome SILVA pertence ao nome? {}".format('SILVA' in nome.upper()))
