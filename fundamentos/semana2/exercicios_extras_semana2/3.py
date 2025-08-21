# Exercício 3 - Use um for para exibir os números de 1 até o número que o usuário pedir.

def sequencia():
    numero = int(input("Digite um número: "))
    for i in range(1,numero+1):
        print(i)

def main():
    print("Início do programa.")
    sequencia()
    print("Fim do programa.")

if __name__ == "__main__":
    main()
