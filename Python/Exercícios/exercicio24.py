# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))

if num1 % 2 == 0:
    if num2 % 2 == 0:
        print("Os números são pares!")
    else:
        print("O número",num1,"é par e o número",num2,"é ímpar")
elif num2 % 2 == 0:
    print("O número",num1,"é ímpar e o número",num2,"é par")
else:
    print("Os números são ímpares")

if num1 >= 0:
    if num2 >= 0:
        print("Os dois números são positivos")
    else:
        print("O número",num1,"é positivo e o número",num2,"é negativo")
elif num2 >= 0:
    print("O número",num1,"é negativo e o número",num2,"é positivo")
else:
    print("Os dois números são negativos")

redondo1 = round(num1)
redondo2 = round(num2)

if redondo1 % num1 == 0:
    if redondo2 % num2 == 0:
        print("Os dois números são inteiros")
    else:
        print("O número",num1,"é inteiro e o número",num2,"é decimal")
elif redondo2 % num2 == 0:
    print("O número",num1,"é decimal e o número",num2,"é inteiro")
else:
    print("Os dois números são decimais")
