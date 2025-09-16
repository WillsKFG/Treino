def contagem_regressiva(numero):
    while (True):
        print(numero)
        numero -= 1
        if numero == 0:
            print("Contagem encerrada")
            break

#contagem_regressiva(10)

def maior_numero(lista_numeros):
    maior_numero = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero


lista = [5, 6, 7, 8, 10, 2, 11, 3]
maior_numero_lista = maior_numero(lista)
print(f"O maior número da lista é {maior_numero_lista}")