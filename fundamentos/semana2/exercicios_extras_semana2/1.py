""" 
def funcao_exemplo(parametro):
    print(f"Executando função com: {parametro}")
    
def main():
    print("Início do programa")
    funcao_exemplo("teste")
    
if __name__ == "__main__":
    main()

Exercício 1

def maior_de_idade():
    idade = int(input("Digite sua idade: "))
    
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

def main():
    print("Início do programa.")
    maior_de_idade()

if __name__ == "__main__":
    main()
    
"""
# Boa prática

def maior_de_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    except ValueError:
        print("Erro: você precisa digitar um número válido.")

def main():
    print("Início do programa.")
    maior_de_idade()
    print("Fim do programa.")
    
if __name__ == "__main__":
    main()