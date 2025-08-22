# Exercício 12 - Crie uma função com valor padrão para um parâmetro.

def preco_com_desconto(preco, desconto=10):
    return preco * (1 - desconto / 100)


def main():
    print("Início do programa.")
    valor_produto = float(input("Digite o valor do produto: "))
    valor_com_desconto = preco_com_desconto(valor_produto)
    print(f"Valor final do produto com desconto: {valor_com_desconto:.2f}")
    print("Fim do programa.")
    

if __name__ == "__main__":
    main()