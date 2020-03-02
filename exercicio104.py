x = 3
y = 5
tmp = x
x = y
y = tmp

a = 1
b = 2

(a,b) = (b,a)
print(a,b)


# Define a funcao
def sum(x=3, y=5):
	print("x: " + str(x))
	print("y: " + str(y))
	return x + y

    # Chamada simples de funcao
x = 1
y = 2
z = sum(x, y)
print(z)


def comparaLista(espaco, tempo):
        if lista1 == lista2:
            print('igual')
            return True
        else:
            print('desigual')
            return False
lista1 = [100,201]
lista2 = [100, 200]
comparaLista(lista1,lista2)

def comparaPol1(palavra1 = "Natan"):
    stringSemEspacos = palavra1.replace(' ', '')
    stringMinuscula = stringSemEspacos.lower()
    stringInvertida = stringMinuscula[::-1]
    if stringInvertida == stringMinuscula:
            return True
    else:
            return False

def comparaPol2(palavra2 = "ovo"):
    stringSemEspacos = palavra2.replace(' ', '')
    stringMinuscula = stringSemEspacos.lower()
    stringInvertida = stringMinuscula[::-1]
    if stringInvertida == stringMinuscula:
            return True
    else:
            return False


if comparaPol1() and comparaPol2() == True:
    print("é palindrome")
else:
    print("num é")


# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
# OBS.: Utilize apenas o que foi estudado ate agora
