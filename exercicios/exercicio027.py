'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''

n = str(input("Digite o nome completo: "))

nome1 = n.split()

print("O primeiro nome é: {} e o último é: {}".format(nome1[0], nome1[len(nome1) - 1]))