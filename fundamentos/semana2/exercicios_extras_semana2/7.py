#  Exercício 7 - Use while para pedir uma senha até que o usuário acerte.

def verificar_senha():
    senha = "ola mundo"
    
    while True:
        adivinha = input("Digite a senha: ")
        if senha == adivinha:
            print("Você acertou a senha!")
            break
        else:
            print("Senha errada! Tente de novo.")
    
def main():
    print("Início do programa")
    verificar_senha()
    print("Fim do programa")
    
if __name__ == "__main__":
    main()