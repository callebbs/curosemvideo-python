# Fatiamento de Strings

#frase = ["Curso em Vídeo Python"]

# frase[9] - Utiliza o caractere que está na posição 9.
# frase[9:13] - Mostra os caracteres que inicia da posição 9 até a 12. (a última não é contada)
# frase[9:21:2] - Mostra os caracteres que inicia na posição 9 até a 20, pulando de dois em dois.
# frase[:5] - Mostra os caracteres do primeiro índice até o 4.
# frase[15:] - Mostra os caracteres do índice 15 até o final.
# frase[9::3] - Mostra os caracteres do índice 9 até o final, pulando de três em três.

#Análise

# len(frase) - Lê a frase e diz quantos caracteres tem.
# frase.count('o') - Conta quantas vezes aparece a letra pedida (neste caso é o "o").
# frase.count('o', 0, 13) - Contagem com fatiamento. Neste exemplo ele conta do 0 até o 12 e faz a contagem.
# frase.find('deo') - Mostra o índice inicial da string pesquisada (Resultado: 11)
# frase.find("Android") - Ao pesquisar por string inexistente, retorna o valor -1.
# "Curso" in frase - Retorna resultado Booleano: True or False

#Transformação

#Alteração de string através de métodos

# frase.replace("Python", "Android") - Substitui a primeira string pela segunda.
