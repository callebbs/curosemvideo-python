'''
Faça um programa que leia um número inteiro e mostra na tela seu sucessor e seu antecessor.
'''

numero = (int(input("Digite um número inteiro: ")))
print(f"Você digitou o número {numero}. Seu anterior é:", numero - 1, "e o sucessor:", numero + 1)

#outra forma de mostrar utilizando .format no final
#print("Você digitou o número {}. Seu anterior é: {} e seu sucessor é {}".format(numero, numero - 1, numero + 1))