'''
	DESAFIO!!!
	1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
	2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999.
    Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''
#1)
print(list(range(1001)[::2]))

#2)
'''
lista = list(range(10))
print(lista)

cont = 0
pos = 1
while cont < 100:
    num = lista[pos]
if num % 5 == 0:
    print(num)
else:
	cont +=1
	pos +=1
'''

#1

letras = ['a', 'b', 'c']

for x in letras:

    print(x.upper())

#2

numeros = [0, 1, 3, 4, 5]
soma = 0
for x in numeros:
    soma = soma + x
print("TOTAL: ", soma)

#3

for x in numeros:
    if x % 2 != 0:
        print(x)

#4

frase = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

lista_frase = []
lista_frase = frase.split(' ')
for x in lista_frase:
    if len(x) >= 5:
        print(x)

#5

multiplos = [ i * 3  for i in range(100)]
for x in multiplos:
    print(x)

#6

numeros_primos = [2, 3, 4, 5, 6, 7, 8, 9 ,10]
for x in numeros_primos:
    if x % 2 != 0:
        print(x , 'numero primo!')
