# Resolução do exercício 5:
# Letras maiúsculas e minúsculas
def check_char(text):
    type = {"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original:", text)
    print("Número de letras maiúsculas: ", type["Uppercase"])
    print("Número de letras minúsculas: ", type["Lowercase"])


check_char("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent fringilla scelerisque nisl, ultricies scelerisque elit iaculis non. Etiam viverra interdum massa, ut semper massa lacinia eget. Curabitur iaculis, arcu quis efficitur ultricies, diam neque gravida magna, ut congue turpis elit sed enim. Sed facilisis, nisl vitae dictum sodales, metus diam faucibus odio, id rhoncus nisi lectus nec urna. Duis volutpat tellus id nibh gravida, eu pretium sem facilisis. Curabitur pharetra magna id enim consequat imperdiet. Mauris diam nisl, molestie vitae libero vitae, commodo rutrum mi. Etiam dignissim ex vitae libero auctor consectetur. Nunc congue sapien eros, in auctor lacus euismod eu. In vitae erat ut lectus luctus blandit. Fusce at ligula quis eros ultricies varius sed a ante. Nunc vel urna eget elit interdum mattis. Proin euismod dignissim aliquam. Suspendisse vestibulum mi ut mauris ornare tempor. Fusce elementum quam vel turpis faucibus, eu scelerisque nulla consectetur. Mauris eget lorem non mauris auctor luctus.")

# Verifica número par ou ímpar


def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd


print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
