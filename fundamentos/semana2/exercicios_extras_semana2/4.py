# Exercício 4 - Use range() para exibir os números pares de 0 a 20.

def numeros_pares():
    for i in range(0,22,2):
        print(i)

def main():
    print("Início do programa.")
    numeros_pares()
    print("Fim do programa.")
    
if __name__ == "__main__":
    main()