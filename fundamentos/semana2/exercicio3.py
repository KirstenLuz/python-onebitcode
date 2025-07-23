"""
* Verificar o conteúdo da string
-> Escreva um programa em Python para verificar se uma string
contém apenas um determinado conjunto de caracteres (neste caso, 
a-z, A-Z e 0-9)

Minha resolução
import re

texto = 
"Barbie em O Lago dos Cisnes" é um filme de animação que reconta a clássica 
história do balé "O Lago dos Cisnes", com a Barbie interpretando a jovem 
Odette. Na trama, Odette, filha -de um padeiro, é transformada em cisne por 
um feitiço do mago Rothbart[], que busca derrotar a Rainha das Fadas. Para 
quebrar o feitiço, Odette precisa da ajuda do príncipe Daniel e enfrentar 
diversos desafios na Floresta Encant+ada. 
Enredo:
A história começa com Odette, uma jovem simples e com pouca autoconfiança, que 
descobre a Floresta Encantada e um unicórnio mágico chamado Lila. Ela encontra 
um cristal que a designa como a salvadora da floresta. Em sua aventura, Odette 
é transformada em cisne por Rothbart, um mago que deseja dominar a Floresta 
Encantada e derro<tar a Rainha das Fadas. 
Para reverter o feitiço, Odette precisa = da ajuda do p^ríncipe Daniel e da 
Rainha das Fadas, enfrentando desafios e provando sua coragem, honestidade 
e inteligência. A trama explora temas como amor verdadeiro, coragem, amizade 
e a importância de acreditar> em si mesmo.

# pattern = r"[+\-=]"
pattern = r"[@#$%&*\(\)\-_=+\{\}\[\]\^~;:<>]"
result = re.findall(pattern, texto)
print(texto)
print(result)
if result:
    print("Há correspondências")
else:
    print("Não há nenhuma correspondência")
"""

# Correção
import re


def check_character(string):
    rule = re.compile(r"[^a-zA-Z0-9]")
    string = rule.search(string)
    return not bool(string)


print(check_character("AajahajhaaajhSUSHAHIAIS123457"))
