#10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
import math

metragem = float(input("Insira a medida de sua área: "))

raio = math.pi * math.pow(metragem,2)

valor = raio * 25.00
print(f'O valor total do pedido ficou em R$ {round(valor,2)}')