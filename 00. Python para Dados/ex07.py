#Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
#"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

import random

user = input("Inisra seu nome para receber seu código: ")

while True:
    token = random.randrange(1000, 9998 + 1)
    if token % 2 == 0: break

print(f"Olá {user}, seu token de acesso é {token}! Seja bem-vindo(a)!")
    