msg = 'Minimal Techno Tripping'
print(msg[::-1])

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

title = book1.find(' by')
print(title)
print(book1[:title])
title1 = book1[:title]
print(len(title1))
print(title1)
print("IIIIIII")
a = book1.replace("by", "-")
print(a)

print('yyyyyyyyyyy')


# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'


string1 = "ovo"
stringSemEspacos = string1.replace(' ', '')
stringMinuscula = stringSemEspacos.lower()
stringInvertida = stringMinuscula[::-1]
if stringInvertida == stringMinuscula:
        print ("SIM")
else:
        print ("NAO")

string2 = "Natan"
stringSemEspacos = string2.replace(' ', '')
stringMinuscula = stringSemEspacos.lower()
stringInvertida = stringMinuscula[::-1]
if stringInvertida == stringMinuscula:
        print ("SIM")
else:
        print ("NAO")

string3 = "luz azul"
stringSemEspacos = string3.replace(' ', '')
stringMinuscula = stringSemEspacos.lower()
stringInvertida = stringMinuscula[::-1]
if stringInvertida == stringMinuscula:
        print ("SIM")
else:
        print ("NAO")

string4 = "caneta azul"
stringSemEspacos = string4.replace(' ', '')
stringMinuscula = stringSemEspacos.lower()
stringInvertida = stringMinuscula[::-1]
if stringInvertida == stringMinuscula:
        print ("SIM")
else:
        print ("NAO")
