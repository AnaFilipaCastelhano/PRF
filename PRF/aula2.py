#lists

lista = ['a', 'b', 1, 2, 3]

print(lista)


#list indexes
#lista[4]=lista[-1]

#list length

len(lista)

#modifying lists

lista[1] = 'c'

#adding or removing values

lista.append('lá')
print(lista)

lista.pop() #tira o ultimo elemento da lista, se n colocar nada dentro do parentises, mas posso tb remover um elemento especifico tendo em conta o seu indice
print(lista)
lista.pop(1)
print(lista)

lista.remove(2)
print(lista)
#lista.remove("abc")

del lista[1] #isto n funciona, se fizer del lista isso sim, apaga a lista completa
print(lista)

#count occurrences

lista.append(3)
print(lista.count(3))
print(lista.count(1))


#find position of something
#make it backwards
#order it
#order with different types?

lista.index(3) # posso dar um start e um end para otimizar a pesquisa, devolve o indice do 3
#lista.sort() # n possos ter str e int, ou só um ou só outro

newList = [1, 3.1, 2, 2]
newList.sort()
print (newList)

#joining lists

nova_lista = lista+newList
print(nova_lista)

nova_lista *=2 #duplica a lista
print(nova_lista)

#nova_lista = nova_lista//2 #isto n funciona
#print(nova_lista)

#printing list data

print(nova_lista[3:5])
print(nova_lista[:-3])

#two dimensions

lista_duas_dim = [[1, 1, 1], [2, 2, 2], [3, 4, 5]]
print(lista_duas_dim)


#printing two dimensions

print(lista_duas_dim[1])
print(lista_duas_dim[2][1])


#loops
#range
#nested loops
#exercise? 2 5 8 11 different solutions?
#what is the output of?

#comparison operators
#conditions
#complex conditions
#conditions in loops
#stoping a loop