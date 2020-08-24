'''
Crie um script em Python que leia dois números e tente mostrar a soma entre eles.
Desafio extra: colocar os números que foram digitados na mensagem final.
'''
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

soma = (numero1 + numero2)

#print("A soma dos números", numero1, "e", numero2, "é:", soma)

print("A soma de {} e {} é igual a {}.".format(numero1, numero2, soma))