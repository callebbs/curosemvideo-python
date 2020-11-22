'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import cos, tan, sin, radians

angulo = int(input("Digite um ângulo qualquer: "))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print("Do angulo {} podemos identificar que seu:\nSeno é de {:.2f}.\nCosseno é de {:.2f}.\nE a Tangente é de {:.2f}.".format(angulo, sen, cos, tan))