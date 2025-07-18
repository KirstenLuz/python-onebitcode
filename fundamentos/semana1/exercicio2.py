"""
Exercícios
1 - Substituindo caractere repetido:
Escreva um programa Python para obter uma string de uma determinada string 
em que todas as ocorrências de seu primeiro caractere foram alteradas para 
'$', exceto o próprio primeiro caractere
Ex: fifa 23 -> fi$a 23

2 - Troca de caracteres
Escreva um programa Python para obter uma única string de duas strings 
fornecidas, separadas por um espaço e troque os dois primeiros caracteres
de cada string.
Ex: abc xyz -> xyc abz

Ex 1.
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean 
sapien metus, volutpat non velit sit amet, sagittis blandit erat. Fusce vel 
nisl mollis, ornare dolor quis, pellentesque dolor. Vivamus cursus velit neque, 
ut imperdiet purus condimentum sit amet. Ut aliquet egestas mi, eu malesuada 
urna. Nunc dictum massa at cursus finibus. Nam commodo sapien eget ipsum dictum 
aliquet. Nullam purus quam, luctus et laoreet vel, facilisis in mauris. 
'

Ex 2.
caractere = texto[0:1].lower()

print(texto[0:].replace(caractere, "$"))


frases = input("Insira duas frases: ")

espaco = frases.find(" ")

caractere_mod = frases[0:1]

print(frases[0:1])
print(frases[espaco:espaco+1])

frases = frases.replace(frases[0], frases[espaco:espaco+1])
frases = frases.replace(frases[espaco+1], caractere_mod)

print(frases)
"""