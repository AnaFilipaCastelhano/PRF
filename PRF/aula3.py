# conditions

variavel = 25

if variavel > 10:
    print("É maior")
else:
    print('É menor')

if variavel < 10:
    print("É menor q 10")
elif variavel > 10 and variavel < 20:
    print("Está entre 10 e 20")
else:
    print('É maior q 20')

if variavel < 10:
    print("É menor q 10")
elif variavel > 20:
    print("É maior que 20")
else:
    print('Está entre 10 e 20')

# And
# TRUE	TRUE	TRUE
# TRUE	FALSE	FALSE
# FALSE	TRUE	FALSE
# FALSE	FALSE	FALSE

# or
# TRUE	TRUE	TRUE
# TRUE	FALSE	TRUE
# FALSE	TRUE	TRUE
# FALSE	FALSE	FALSE


# pass

if variavel < 10:
    print("É menor q 10")
elif variavel > 20:
    pass  # passa à frente e não faz nada ainda que a condição seja verdadeira e faz cm q n dê erro
else:
    print('Está entre 10 e 20')

# single line conditions


if variavel > 25: print("It is hot")
print("It is hot") if variavel > 25 else print("It is not hot")  # IMPORTANTE
print("it is hot") if variavel > 25 else print("it is cold") if variavel < 10 else print("it is ok")

# nested conditions (if dentro de um if)

if variavel < 10:
    print("É menor q 10")
    if variavel < 5:
        print("Está frio!")
elif variavel > 20:
    print("É maior que 20")
else:
    print('Está entre 10 e 20')

temperature = 27
if temperature > 25:
    if temperature > 26:
        print("stuff")
    print('it is hot')  # se a temperatura entrar nas duas condições imprime ambos, stuff e it is hot
else:
    print('it is not hot')

# complex conditions
# loops

frase = "hoje está frio"

for letra in frase:
    print(letra)

lista = ["a", "b", "c", 1, 2, 3]

for elemento in lista:
    print(elemento)

# range

for indice in range(0, 2):  # inclusive o primeiro, exclusive o segundo
    print(lista[indice])

for indice in range(2):  # se der um parametro estou a dar o fim (exclusive); com 2 parametro dá o inicio e o fim
    print(lista[indice])

for indice in range(1, 6, 2):  # inicio e fim e de quantos em quantos anda ( o fim é sempre exclusive)
    print(lista[indice])

for indice in range(0, len(lista), 2):
    print(lista[indice])

for indice in range(len(lista)):
    if indice > 3:
        break  # para o for quando chega ao indice 3
    print(lista[indice])

for indice in range(len(lista)):
    if indice == 3:
        continue  # omite o indice 3
    print(lista[indice])

# more loops
# nested loops

adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adjectives:  # para cada iteração do primeiro ele executa o segundo for para todos os elementos da lista
    for j in fruits:
        print(i, j)

# exercises

# criar lista com duas dimensoes (7:3)
# de duas em duas entradas da primeira dimensão, somar a segunda dimensão e imprimir o resultado
# se a soma for par, imprimir "é par"


lista = [[1, 2, 3], [3, 4, 5], [7, 8, 9], [10, 11, 12], [13, 14, 16], [16, 17, 18], [19, 20, 21]]

# for indice in range(len(lista)):
#    if indice % 2 == 0:
#        soma = 0
#        for i in lista[indice]:
#            soma += i
#        if soma % 2 == 0:
#            print(soma)
#            print("Par")
#        else:
#            print("Impar")


for indice in range(0, len(lista), 2):
    soma = 0
    for i in lista[indice]:
        soma += i
    if soma % 2 == 0:
        print(soma)
        print("Par")
