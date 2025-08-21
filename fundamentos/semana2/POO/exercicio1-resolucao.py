# Resolução
class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"

    def technical_sheet(self):
        print("\nDados do filme")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação do filme: {self.totalEvaluation}")
        print(f"Total de avaliadores: {self.evaluators}")
        print(f"Duração do filme: {self.durationMinutes}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(
            f"""Média do filme: {self.name} - {self.totalEvaluation / self.evaluators}""")


mario = Movie("Super Mario Bros", 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10)
mario.evaluate(8.5)
mario.evaluate(4)
mario.evaluate(7)
mario.evaluate(7.5)
mario.evaluate(4)
mario.average()
