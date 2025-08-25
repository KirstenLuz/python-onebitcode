# Exercício 15 - Crie uma função lambda que calcule o quadrado de um número.

def main():
    number = int(input("Digite um número: "))
    power = lambda num: num ** 2
    print(power(number))

if __name__ == "__main__":
    main()