# declaring variables

a = 10
a = "abc"
# posso mudar o tipo da variável sem problema

# print(a)

b = c = 10

# assigning values
# constants

# existem variáveis mas elas podem sempre mudar de valor, normalmente constantes, noutras linguagens escrevem-se em letras maiusculas

A = 10
PI = 3.1475  # float é cm ponto e n virgula
PI = 2  # o python n faz validação apesar de ser uma constante
# print(PI)

# good practices

# os nomes devem ser o mais descritivo possivel, tipicamente em inglês,
# não se usem caracteres especiais,
# nomes das variaveis em camel notation ou cm underscores,
# não declarar coisas no meio do código variaveis devem ser sempre declaradas no inicio, ou então em contextos especificos por exemplo uma variável pode ser exclusiva a um determinado ciclo ou a uma determinada class, variáveis para usar em vários sitios devem ser declaradas no inicio para ser mais fácil de ler
# comentários são muitissimo importantes nomeadamente para explicar para q vou usar determinadas variáveis,
# funções devem ser o mais pequenas possiveis (muito importante) e tentar q tenham uma única responsabilidade, só devem fazer uma única coisa, ex máquina de calcula uma função especifica para soma, outra para multiplicar, etc
# não abusar da largura do ecrã, mesmo no q toca a comentários
# ctrl+alt+l - formata o código



del PI
# print(PI)


# arithmetic operators

a = 10
a += 1  # ou a = a+1
print(a)

# / coeficiente da divisão
# % resto da divisão ou modulo
# // valor inteiro da divisão
# se print(-d) fico com o valor da variável negativo


# errors

# não é possivel concatnar um inteiro com uma string
# tb pode acontecer a varável n estar definidida, ...


# variable type


# o python identifica automáticamente o tipo

print(type(
    a))  # pode ser útil para validar o input do utilizador, tudo pode ser convertido para str mas nem tudo pode ser convertifo para int

# floats

v = 1.1 + 2.2
print(v == 3.3) # avalia a condição e retorna True ou False, primeiro avalia o q tá dentro de parentises e depois o q está fora

#o python guarda mais ou menos o valor dos floats, n guarda exatamente o valor certo
#para comparar flots tenho q definir uma determinada tolarância, considero q é igual se o valor da diferença for mais pequeno q a minha tolerância

tolerance = 0.00001
x = 1.1 + 2.2
print(abs(x - 3.3) < tolerance)


# converting types

#funções usadas para isto: int(), float(), str()

f = "número: "
f = f+str(1)
print(f)

myVar = int("1")
print(type(myVar))





# combining text
# lists
# variable type
# list indexes
# list length
# errors
# modifying lists
# adding or removing values
# some operations are only for list
# count occurrences
# find position of something
# make it backwards
# order it
# order with different types?
# joining lists
# printing list data
# two dimensions
# printing two dimensions

# loops
# range
# nested loops
# exercise
