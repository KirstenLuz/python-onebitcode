# 18. Adicione um novo par chave-valor ao dicionário.

escovaPhilco = {
    "price": 799.90,
    "yearLaunch": 2025,
    "version": 4
}

nova_chave = input("Digite a nova chave: ")
novo_valor = float(input(f"Digite o valor da chave '{nova_chave}': "))

escovaPhilco[nova_chave] = novo_valor
print(escovaPhilco)
