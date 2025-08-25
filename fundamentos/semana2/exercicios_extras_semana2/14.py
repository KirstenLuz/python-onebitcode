# Exercício 14: Crie uma função que receba **kwargs e exiba as chaves e valores.

def floricultura(**flores):
    print("Detalhes do pedido:")
    for chave, valor in flores.items():
        print(f"{chave.capitalize()}: {valor}")


def main():
    print("Início do programa.")
    floricultura(tipo="rosas", cor="vermelha", quantidade=12)
    print("Fim do programa.")
    
if __name__ == "__main__":
    main()
    
