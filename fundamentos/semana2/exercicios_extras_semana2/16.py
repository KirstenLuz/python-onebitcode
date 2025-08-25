# Exercício 16 - Use função lambda para inverter uma string.

def main():
    reverse_string = lambda string: string[::-1]
    
    user_string = input("Digite uma frase: ")
    print(reverse_string(user_string))
    

if __name__ == "__main__":
    main()