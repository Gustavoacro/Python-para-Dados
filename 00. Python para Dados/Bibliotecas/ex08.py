#8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
import random

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

sorteador = random.sample(frutas,3)
print(f"Os sabores da sua salada de fruta serão: {sorteador}")
print(f"A salada surpresa é: {sorteador[0]}, {sorteador[1]} e {sorteador[2]}")
