# 17. Atualize o preço de um produto no dicionário.

escovaPhilco = {
    "price": 799.90,
    "yearLaunch": 2025,
    "version": 4
}

"""
preco = float(input("Digite o novo valor da Escova Philco: "))

escovaPhilco["price"] = preco
print(escovaPhilco)
"""

escovaPhilco.update({"price": 654.7})
print(escovaPhilco)
