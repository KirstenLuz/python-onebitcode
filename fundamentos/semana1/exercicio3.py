"""
Exercícios 3:
- Cálculo da distância
Escreva um programa que pergunte a distância que um
passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

- Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e
calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, de 15%.

1.
km = float(input("Qual a distância percorrida (km): "))

if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.35

print(f"O valor da passagem é R$ {passagem}")
"""

salario = float(input("Digite seu salário: "))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.1

print(f"Seu aumento será de {aumento} reais.")
