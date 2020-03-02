weekdays = ['mon','tues','wed','thurs','fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
print(days)
days = weekdays[0:3]       # elementos 0, 1, 2
print(days)
days = weekdays[:3]        # elementos 0, 1, 2
print(days)
days = weekdays[-1]        # ultimo elemento
print(days)
test = weekdays[3:]        # elementos 3, 4
print(test)

print('iiiiiii')
days = weekdays[-2]        # ultimo elemento (elemento 4
print(days)
days = weekdays[::]        # all elementos
print(days)
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)******
print(days)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)
print(days)

all_days = weekdays + ['sat','sun']     # concatenar

print(all_days)

print('iiiiiiiiiiiiiii')
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))
# list.reverse()
# print(list)

print('eeeeeeeeeeeeee')
# Como selecionar 'wed' pelo indice?

days = weekdays[2]
print(days)

# Como verificar o tipo de 'mon'?

days = weekdays[0]
print(days)
print(type(days))

# Como separar 'wed' até 'fri'?

days = weekdays[2:]
print(days)

# Quais as maneiras de selecionar 'fri' por indice?
days = weekdays[4]
print(days)
days = weekdays[-1]
print(days)

# Qual eh o tamanho dos dias e days_list?
print(len (days_list))
print(len (days_list[0]))
print(len (days_list[1]))
print(len (days_list[2]))
print(len (days_list[3]))
print(len (days_list[4]))
print(len (days_list[5]))
print(len (days_list[6]))

# Como inverter a ordem dos dias?

days1 = days_list[::-1]      # reverso (4, 3, 2, 1, 0)
print(days1)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?

list.insert(1, 'zero')
print(list)

# Como limpar list?

list.clear()
print(list)

# Como deletar list?

del(list)
print(list)
print('ooooo')

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
list = ['a', 1, 3.14159265359]
ultimo_elemento = list[-1]
del(list[-1])
print(list)
print(ultimo_elemento)
