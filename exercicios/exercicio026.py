'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input("Digite uma frase qualquer: ")).strip()

print("Na frase {}, a letra A aparece {} vezes.".format(frase, frase.lower().count('a')+1))
print("Esta letra aparece no índice {}. ".format(frase.lower().find('a')+1))
print("Esta letra também aparece por último no índice {}".format(frase.lower().rfind('a')+1))