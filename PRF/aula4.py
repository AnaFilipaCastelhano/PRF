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
# funcoes fazem APENAS uma coisa

def funcao(atributo):
    return atributo


def celcius_to_fh(grausc):
    return ((9 / 5) * grausc) + 32


def kelvein_to_cel(kelvein):
    return kelvein - 273.15


def klv_to_fh(klv):
    return celcius_to_fh(kelvein_to_cel(klv))


# função q recebe um nº variavel de argumentos, nota: os argumentos são interpretados como uma lista
def var_argumentos(*inteiros):
    soma = 0
    for i in inteiros:
        soma += i
    return soma


print(var_argumentos(1, 2, 3, 4, 5, 6, 7, 8))


# quando me pedem número garantir que faço validação do input

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



