# Exercício 2 - Receba um número e informe se ele é par ou ímpar.

def par_ou_impar():
    try:
        numero = float(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    except ValueError:
        print("Erro: você deve digitar um número!")

def main():
    print("Início do programa.")
    par_ou_impar()
    print("Fim do programa.")
    
if __name__ == "__main__":
    main()