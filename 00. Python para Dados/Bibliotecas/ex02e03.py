#2.Escreva um código para importar a biblioteca numpy com o alias np.
#3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

import numpy as np
from random import choice as chs

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

sorteador = chs(lista)

print(sorteador)

