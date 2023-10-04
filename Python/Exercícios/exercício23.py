# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num = float(input("Informe um núemro: "))

redondo = round(num)

if redondo % num == 0:
    print("Este número é inteiro!")
else:
    print("Este número é decimal!")

