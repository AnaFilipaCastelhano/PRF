# utilizo while quando n sei ao certo quando vou ter q parar
# while tb é interessante quando preciso de inputs do utilizador


# not (A or B) = (not A) and (not B)
# not (A and B) = (not A) or (not B)
# https://en.wikipedia.org/wiki/De_Morgan%27s_laws


# more loops
# nested loops


odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [10, 4, 6, 8, 2]
printed_numbers = 0
for i in range(0, len(odd_numbers), 2):
    print(odd_numbers[i] + even_numbers[i])
    printed_numbers += 1
else:
    print(printed_numbers)


# funções
#funcoes fazem APENAS uma coisa

def funcao(atributo):
    return atributo


def celcius_to_fh(grausc):
    return ((9 / 5) * grausc) + 32


def kelvein_to_cel(kelvein):
    return kelvein - 273.15


def klv_to_fh(klv):
    return celcius_to_fh(kelvein_to_cel(klv))


#função q recebe um nº variavel de argumentos, nota: os argumentos são interpretados como uma lista
def var_argumentos(*inteiros):
    soma = 0
    for i in inteiros:
        soma += i
    return soma

print(var_argumentos(1,2,3,4,5,6,7,8))

#quando me pedem número garantir que faço validação do input

def insere_num():
    lista = []
    numero = -1
    while numero != 0:
        try:
            numero = int(input("Enter number: "))
            lista.append(numero)
        except ValueError:
            print("Not an integer!")

insere_num()

#funções para fazer isto, documentado e com os nomes todos certos:
# join two lists of strings based on the index
# find top N element(s) in list ( o N vai ser definido pelo utilizador)
# encontrar o maior elemento de uma lista


names1 = ["a", "b", "c", "d", "e", "f"]
names2 = ["g", "h", "i", "j", "k", "l"]

def join_lists(list1, list2):
    new_list = []                                   #this creats a empty list, so the pars can be added
    for element1, element2 in zip(list1,list2):     #for cicle iterates for both lists at the same time, and will append the par of elements as a tuple, on the new list
        new_list.append((element1, element2))
    return new_list

print(join_lists(names1, names2))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30]

def find_highest_number(list):
    container = list[0]                             #this creats a variable where the highest number should be stored, and it is inicialized with the 1st element of the list
    for number in list:                             #for cicle will iterate for all elements on the list
        if number > container:                      #for every element on the list if function tests is it is greater then the number on the container
            container = number                      #if the number we are analysing turns out to be greater, it is used to replace the value on the container
    return container

print(find_highest_number(numbers))
