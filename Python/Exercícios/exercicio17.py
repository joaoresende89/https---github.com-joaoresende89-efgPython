# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("Informe um ano: "))

if (ano % 100 != 0) and ((ano % 4 == 0) or (ano % 400 == 0)):
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")

