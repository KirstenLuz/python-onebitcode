# Exercício 6 - Peça 5 notas e calcule a média.
""" 
Meu código

def pedir_notas():
    lista_notas = []
    print("Digite suas notas abaixo: ")
    for i in range(5):
        nota = float(input(f"{i+1}º nota: "))
        lista_notas.append(nota)
    return lista_notas

def media(notas):
    media_final = sum(notas) / len(notas)
    print(f"A sua média é: {media_final}")

def main():
    print("Início do programa.")
    notas = pedir_notas()
    media(notas)
    print("Fim do programa.")
    
if __name__ == "__main__":
    main()

"""

""" 
Regras principais sobre espaçamento entre funções:
- Entre funções e classes de nível superior (como def pedir_notas(...) e def calcular_media(...)), você deve deixar 2 linhas em branco.
- Dentro de uma classe, entre métodos, você deixa 1 linha em branco.
- Dentro de uma função, você não deve deixar linhas em branco desnecessárias (só se for para separar blocos lógicos e ajudar na legibilidade).
"""

# Boas práticas
# constante configurável: quantidade de notas a serem pedidas - deixar "números mágicos" (como 5) em constantes nomeadas.
QTD_NOTAS = 5 


def pedir_notas(qtd=QTD_NOTAS):
    """
    Pede ao usuário uma quantidade de notas (default: QTD_NOTAS) e retorna uma lista de floats.
    Função genérica -> pode pedir 5, 10 ou qualquer quantidade de notas.
    """
    lista_notas = []
    print("Digite suas notas abaixo: ")
    for i in range(qtd):
        # usar append() em vez de acessar índices diretamente em lista vazia
        nota = float(input(f"{i+1}º nota: "))
        lista_notas.append(nota)
    return lista_notas


def calcular_media(notas):
    """
    A função retorna o valor em vez de só imprimir.
    Isso torna a função mais reutilizável em outros programas.
    """
    return sum(notas) / len(notas)


def main():
    """
    Separar a lógica em funções auxiliares e manter o main "limpo".
    """
    print("Início do programa.")
    notas = pedir_notas(QTD_NOTAS)  # Coleta notas do usuário
    media = calcular_media(notas)   # Calcula média
    print(f"A sua média é: {media:.2f}")  # ✅ :.2f formata para 2 casas decimais
    print("Fim do programa.")


if __name__ == "__main__":
    main()
