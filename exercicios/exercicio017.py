'''
Faça um prograama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, caslcule e mostre o comprimento da hipotenusa.
'''

from math import hypot
cateto1 = float(input("Digite o comprimento do cateto oposto: "))
cateto2 = float(input("Digite o comprimento do cateto adjacente: "))

hipo = hypot(cateto1, cateto2)

print("A hipotenusa dos catetos {} e {} é de {:.2f}".format(cateto1, cateto2, hipo))