# 20. Acesse e exiba apenas o gênero do segundo livro do dicionário aninhado.

books = {
    "A Vida Invisível de Addie Larue": {
        "yearLaunch": 2024,
        "classification": 4.7
    },
    "Amor, teoricamente": {
        "yearLaunch": 2023,
        "classification": 4.8
    }
}

print(books)
books["A Vida Invisível de Addie Larue"]["genre"] = ["romance", "fantasia"]
books["Amor, teoricamente"]["genre"] = ["romance", "comédia"]
print(books)
