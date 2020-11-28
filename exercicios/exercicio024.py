'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

cidade = str(input("Digite o nome de uma cidade: ")).strip()
print("Analisando o a cidade...")
print("O nome SANTO faz parte do nome da cidade {}?".format(cidade), 'SANTO' in cidade.upper())