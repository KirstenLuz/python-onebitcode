"""
Adivinhe o Número
Escreva um programa em Python que gera um número aleatório para que o usuário 
tente acertar o número. Algumas sugestões para o programa:
Utilizar um laço de repetição para que o programa execute até que o usuário 
informe um número referente a opção para sair do programa.
Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. 
Ex: 1 a 10.
Lê o número que o usuário digitar via input e comparar se é o mesmo número que 
o programa sorteou.

Minha solução:
import random
i = False

while i != True:
  print(\nSelecione a opção: \n
  1. Adivinhe o número\n
  2. Sair\n)

  choice = input("> ")

  if choice == "1":
    r1 = random.randint(1, 10)
    print(r1)
    number = int(input("\nAdivinhe o número de 1 a 10: "))
    if r1 == number:
      print(f"\nVocê o descobriu! O número é {r1}.")
    else:
      print(f"\nVocê errou! O número é {r1}.")
  elif choice == "2":
    i = True
  else:
    print("Resposta inválida, digite novamente.")
"""

# Correção
import random

done = False

# enquanto não verdadeiro (melhor)
while not done:
    print("O que você deseja fazer?")
    print("1. Advinhar o número")
    print("2. Sair")

    choice = input("> ")

    if choice == "1":
        print("=====Advinhe um número de 1 a 10======\n")
        number = int(input("Digite um número de 1 a 10\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns. Você acertou!")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 e 2")

"""
import random

def menu():
    print("\nO que você deseja fazer?")
    print("1. Adivinhar o número")
    print("2. Sair")

def jogar_adivinhacao():
    print("\n===== Adivinhe um número de 1 a 10 =====")

    while True:
        try:
            numero = int(input("Digite um número de 1 a 10: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Por favor, digite um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    resultado = random.randint(1, 10)
    if numero == resultado:
        print(" Parabéns! Você acertou!")
    else:
        print(f" Tente novamente. O número sorteado foi {resultado}.")

def main():
    while True:
        menu()
        escolha = input("> ")

        if escolha == "1":
            jogar_adivinhacao()
        elif escolha == "2":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1 ou 2.")

main()
"""
