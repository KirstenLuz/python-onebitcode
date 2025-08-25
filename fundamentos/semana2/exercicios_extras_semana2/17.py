def insert_list():
    entrada = input("Digite os números separados por espaço: ")
    return [int(x) for x in entrada.split()]


def sorted_list(lista):
    return sorted(lista)  # nova lista ordenada


def main():
    print("Início do programa.")
    numbers_list = insert_list()
    numbers_list_sorted = sorted_list(numbers_list)
    
    print(f"Sua lista original: {numbers_list}")
    print(f"Sua lista ordenada: {numbers_list_sorted}")
    print("Fim do programa.")


if __name__ == "__main__":
    main()
