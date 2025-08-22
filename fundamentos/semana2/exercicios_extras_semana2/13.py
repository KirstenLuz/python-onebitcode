# 13. Crie uma função que receba *args e imprima todos os valores.

def estante_livros(*livros):
    print("\nEstante de livros: ")
    for livro in livros:
        print(f'{livro}')

def main():
    print("Início do programa.")
    
    livros_usuario = []
    while True:
        livro = input("Digite o nome de um livro (ou 'sair' para finalizar): ")
        if livro.lower() == "sair":
            break
        livros_usuario.append(livro)
    
    estante_livros(*livros_usuario)
    # Passar o parâmetro como args faz com que ele desempacote a lista em argumentos
    print("Fim do programa.")


if __name__ == "__main__":
    main()