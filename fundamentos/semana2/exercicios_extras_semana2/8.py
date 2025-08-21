# Exercício 8 - Crie uma lista com números de 1 a 10 e use list comprehension para criar outra lista apenas com números pares.

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]


def main():
    print("Início do programa.")
    lista = list(range(1,11))
    pares = filtrar_pares(lista)
    print(pares)
    print("Fim do programa.")
    
    
if __name__ == "__main__":
    main()