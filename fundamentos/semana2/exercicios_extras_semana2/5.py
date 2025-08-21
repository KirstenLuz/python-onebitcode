# Exercício 5 - Percorra uma lista de nomes usando enumerate() e exiba índice e nome.

barbie_filmes = [
    "Barbie em O Quebra-Nozes",
    "Barbie como Rapunzel",
    "Barbie e o Lago dos Cisnes",
    "Barbie e a Princesa e a Plebeia",
    "Barbie Fairytopia",
    "Barbie e a Magia de Aladus"
]

def lista_indice(lista):
    for i, name in enumerate(lista):
        print(f"{i+1} -> {name}")
        
def main():
    print("Início do programa.")
    lista_indice(barbie_filmes)
    print("Fim do programa.")

if __name__ == "__main__":
    main()
    