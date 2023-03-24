# print("Olá"[0:2])
#
# nome1 = "Carla"
# nome2 = "Lourenço"
# idade1 = "41"
# idade2 = "35"
# receba = input("Escreva um número: ")
# print(receba)

#numero1 = float(input("Escreva um número: \n"))
# numero2 = float(input("Escreva um número: \n"))
# resultado = numero1/numero2
#print(round(resultado,3))
#print("{:.2f}".format(resultado))
# print(f"O resultado é: {resultado:.2f}")

# nome = '''"Olá sou a a 'A'na"'''
# print(nome)

#cidadeDaAna = "Portalegre"

#NIF = 123123123

# cidade = input("Qual a cidade em que nasceu?")
# animal = input("Qual o nome do animal de estimação?")
#
# print(f"O nome da sua banda é: {cidade} {animal}")

# +
# -
# *
# /
# **
# %
# //
#
# pemdas parentises, expoente, multiplicação, divisão, adição e substração


#print(3*3+3//(3-3))


# numero = int(input("Insira um número:"))
# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Impar")


# numero = input("Insira um número:")
# numero1 = int(numero[0])
# numero2 = int(numero[1:3])
# print(numero1+numero2)

# projeto 1 - calculadora de imc (ver a formula no google)
# projeto 2 - quantas semanas tenho de vida se viver até aos 90 anos , quantos dias, quantos meses
# projeto 3 - perguntar total da conta, gorjeta(10%,12% ou 15% - n é com if e else mas vai funcionar cm qq número),quantas pessoas, retorna quanto é q cada um vai pagar
#tentar usar mais o f string e os rounds( os varios tipos)

#projeto 1

peso = int(input("Insira o peso: \n"))
altura = int(input("Insira a altura: \n"))


print(f"O IMC é: {(peso/(altura**2)):.3f}")

#projeto 2

idade = int(input("Insira idade: \n"))


print(f"Se viver até aos {idade} anos, terá {idade*12} meses, {idade*52} semana e {idade*365} dias de vida!")

#projeto 3

total = float(input("Qual o valor a pagar? \n"))
gorjeta = float(input("Qual o valor, em percentagem, de gorjeta a adicionar? \n"))
pessoas = int(input("Quantas pessoas? \n"))


print(f"Cada elemento deverá pagar {((total*(1+(gorjeta/100)))/pessoas):.2f}€")





