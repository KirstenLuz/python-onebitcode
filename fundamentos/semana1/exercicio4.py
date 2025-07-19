"""
Exercício 4:
Contagem regressiva
-> Faça um programa parar escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10, 9, 8,..., 1, 0 e disparar um "beep".

Tabuada
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
"""

# Contagem regressiva
cont = 10

print("Contagem regressiva do lançamento: ")
while (cont != -1):
    print(cont)
    cont -= 1
print("BEEP")

# Tabuada
num = int(input("Diga o número da tabuada: "))
valor_inicial = int(input("Valor inicial: "))
valor_final = int(input("Valor final: "))

print(f"Tabuada do {num}")
for i in range(valor_inicial, valor_final+1):
    print(f"{num}x{i} = {num*i}")
