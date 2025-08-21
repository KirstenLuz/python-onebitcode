"""
Avaliação e Média da Nota de Filmes
Desenvolva novas funcionalidades para complementar o nosso gerenciamento da 
classe Filmes. Segue o escopo das funcionalidades:
1. Uma das funcionalidades requeridas é que o usuário possa realizar a 
avaliação de um filme passando uma nota com parâmetro e que essa nota seja 
salva no atributo específico da classe. 
2. Assim que uma avaliação for realizada, deve ser incrementado o total de 
avaliadores daquele filme. Obs: Considere criar um atributo específico 
para esse fim. 
3. Para cada filme ter uma nota de avaliação média que consiste na divisão 
do total de avaliação pelo total 
de avaliadores.
"""


class Movie:
    def __init__(self, name, yearLaunch, durationMinutes, avaliations,
                 note):
        self.name = name
        self.yearLaunch = yearLaunch
        self.durationMinutes = durationMinutes
        self.avaliations = avaliations
        self.note = self.note

    def __str__(self):
        return f"Filme: {self.name}"

    def grade_average(self, individualNote):
        self.individualNote = individualNote
        self.avaliations += 1
        totalNotes += individualNote
        return (totalNotes/self.avaliations)

    def technical_sheet(self):
        print("\nDados do filme")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Duração do filme: {self.durationMinutes}")
        print(f"Quantidade de avaliações: {self.avaliations}")
        print(f"Avaliação do filme: {self.note}\n")


mario = Movie("Super Mario Bros")
mario.grade_average(4.5)
mario.grade_average(4)
mario.grade_average(2.5)
mario.grade_average(1.5)
mario.grade_average(3.2)
mario.technical_sheet()
