'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços). 
- Quantas letras tem o primeiro nome.
'''

nome = str(input("Digite o nome completo de uma pessoa: "))
print('*' * 40)
print("Analisando o nome digitado...")
print('*' * 40)
print("Nome todo maiúsculo:", nome.upper())
print("Nome todo minúsculo:", nome.lower())
print("Sem considerar espaços, o nome {} tem {} letras.".format(nome, len(nome)-nome.count(' ')))
print("O primeiro nome {} tem {} letras.".format(nome.split()[0], len(nome.split()[0])))
print("Fim da análise de nome.")
print('-' * 40)