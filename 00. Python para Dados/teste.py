# Notas do(a) estudante
notas = [8.5, 9.0, 6.0, 10.0]

def media(lista):
    calculo = sum(lista) / len(lista)
    return(calculo)

resultado = media(notas)

print(type(resultado))