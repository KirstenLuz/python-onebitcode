# Exercício 9 - Use try/except para evitar erro de divisão por zero.

def divisao():
    while True:   
        dividendo = int(input("Digite o valor a ser dividido: "))
        divisor = int(input("Digite o divisor: "))
        try:
            return (dividendo/divisor)
        except ZeroDivisionError:
            print("O divisor não pode ser 0! Digite novamente.")


def main():
    print("Início do programa.")
    resultado = divisao()
    print(f"A divisão é {resultado:.2f}.")
    print("Fim do programa.")

if __name__ == "__main__":
    main()