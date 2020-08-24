'''
Operadores Aritméticos

+ = soma
- = subtração
* = multiplicação
** = potenciação
/ = divisão completa
// = divisão inteira
% = resto da divisão

-----------------------------------

Ordem de Precedência

1 - ( )
2 - **
3 - * / // %
4 - + -

-----------------------------------

Raizes quadradas e cúbicas

25 ** (1/2)
25 ** (1/3)

-----------------------------------
Alinhamento dentro da formatação:

#print(f'Prazer {nome:>20}, seja bem vindo!')

> alinhado a direita
< alinhado a esquerda
^ centralizado
= antes do sinal para adicionar ao texto

#print(f'Prazer {nome:=^20}, seja bem vindo!')

'''
#primeiro código
#nome = input("Qual o seu nome? ")
#print(f'Prazer {nome:=^20}, seja bem vindo!')

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

soma = numero1 + numero2
multi = numero1 * numero2
divi = numero1 / numero2
divint = numero1 // numero2
exp = numero1 ** numero2

print(f"A soma é: {soma}, o produto é: {multi} e a divisão é: {divi:.3f}")
print(f"A divisão inteira é: {divint} e a potência é: {exp}")

#formatar o resultado float: :.3f
#.3 diminuindo para 3 casas decimais e f de float
