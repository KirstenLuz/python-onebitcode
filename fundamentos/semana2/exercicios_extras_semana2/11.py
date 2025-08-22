# Exercício 11 - Crie uma função que calcule o fatorial de um número.

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num-1)

    
def main():
    print("Início do programa.")
    num = int(input("Digite um número: "))
    resultado = fatorial(num)
    print(f"O fatorial de {num} é: {resultado}")
    print("Fim do programa.")


if __name__ == "__main__":
    main()