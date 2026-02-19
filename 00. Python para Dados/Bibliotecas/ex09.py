#9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
import math

numeros = [2, 8, 15, 23, 91, 112, 256]
cont = 0

while cont < len(numeros):
    valor = numeros[cont]
    raiz = math.sqrt(valor)
    
    if raiz.is_integer():
        print(f'O valor {valor} possui raiz quadrada de {raiz:.1f}. A raiz é inteira.')
    else:
        print(f'O valor {valor} possui raiz quadrada de {raiz:.1f}. A raiz é não é inteira.')

    cont += 1