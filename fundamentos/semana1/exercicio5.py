"""
Exercício 5:
Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba uma string e conte o número de
letras maiúsculas e minúsculas desta string.

Lista número pares e impares de uma lista
-> Escreva uma função Python para imprimir os números pares e ímpares
em duas listas separadas para cada uma
"""


def par_impar(a, b):
    lista_par = []
    lista_impar = []
    for i in range(a, b):
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)

    print("Pares: ", lista_par)
    print("Ímpares: ", lista_impar)


par_impar(7, 22)
