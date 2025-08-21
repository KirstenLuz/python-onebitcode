"""
Classe Produto e método desconto
Desenvolva uma classe em Python para atender as seguintes especificidades 
de um Produto:
- Cada produto deve ter um preço e um nome.
- A classe deve ter um método construtor e o método dundle str.
- A classe deve ter um método para desconto. O método recebe o desconto em 
percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0

    def __str__(self):
        return f"Produto: {self.name}"

    def final_price(self, value):
        self.discount = value
        # return f"Produto com desconto: {(self.price*self.discount)/100}"
        self.price = self.price - (self.price*self.discount/100)

    def technical_sheet(self):
        print(f"Nome do produto: {self.name}")
        print(f"Valor do produto: {self.price}")


book = Product("The Invisible Life of Addie Larue", 15.90)
book.final_price(20)
book.technical_sheet()
