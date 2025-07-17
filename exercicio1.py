"""
Exercícios
1. Antecessor e sucessor
Escreva um programa que leia um número e represente o número antecessor
e sucessor dele, utilizando operadores de atribuição
2. Média de 4 notas
Escreva um programa em python que leia quatro números e calcule a média
entre esses números

1.
num = int(input("Digite um número: "))
num -= 1
print(f"Antecessor: {num}")
num += 2
print(f"Sucessor: {num}")
"""

# 2.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))

media = (num1 + num2 + num3 + num4) / 4

print(f"A média dos números é {media}")
