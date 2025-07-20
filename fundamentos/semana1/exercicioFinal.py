"""
Gerenciamento de Jogadores e Times
Escreva um programa em python que realize o gerenciamento de jogadores. Ele 
deve atender aos seguintes requisitos:
- Adicionar um time
- Remover um time
- Listar times
- Adicionar jogador em um time
- Remover jogador de um time
- Listar jogadores de um time
* A opção de listar os times deve mostrar o índice, o nome e a quantidade 
de jogadores do time.
* A opção de adicionar um time deve pedir um nome para o time que será 
cadastrado.
* A opção de remover um time deve pedir o índice específico do time que 
foi cadastrado para fazer a sua exclusão.
* A opção de adicionar um jogador em um time deve pedir um índice do time 
que foi cadastrado e associar com o nome do jogador que será adicionado.
* A opção de remover um jogador em um time deve pedir um índice do time que 
foi cadastrado e utilizar esse índice para remover o jogador que fora 
cadastrado no time.
* A opção de listar os jogadores de um time deve ser informado o índice de um 
time e listar os jogadores que foram associados a ele.

Este é o exercício de revisão do módulo, então aproveite para utilizar todos 
os recursos vistos até agora, como os funções, condições, loop, listas, etc.
"""
teams = {}
done = False

while not done:
    # Opções no programa
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    
    