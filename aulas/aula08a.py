'''
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

#arredondar para cima math.ceil
print('A raiz de número {} é de {}'.format(num, math.ceil(raiz)))

#arredondar para baixo math.floor

print('A raiz de número {} é de {}'.format(num, math.floor(raiz)))

----------------------------------------------------------------------
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de número {} é de {:.2f}'.format(num, floor(raiz)))


import random

num = random.random()
print(num)
'''

import random
num = random.randint(1, 10)
print(num)