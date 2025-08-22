# Exercício 10 - Capture ValueError ao tentar converter entrada inválida para int.

def usuario():
    while True:
        try:
            nome_usuario = input("Digite seu nome completo: ")
            cpf_usuario = int(input("Digite seu CPF: "))
            return f"Nome: {nome_usuario}\nCPF: {cpf_usuario}"
        except ValueError:
            print("Entrada inválida! Digite novamente.")
    


def main():
    print("Início do programa.")
    dados = usuario()
    print("Dados do usuário")
    print(dados)
    print("Fim do programa.")


if __name__ == "__main__":
    main() 
