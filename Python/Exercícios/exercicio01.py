# Faça um Programa que peça dois números e imprima o maior deles.

n1 = input("Informe um número: ")
n2 = input("Informe um néumro: ")

try:
    n1 = int(n1)
    n2 = int(n2)

    if n1 > n2:
        print("O número maior é: ", n1)
    elif n1 == n2:
        print("Os números são iguais!")
    else:
        print("O número maior é: ", n2)
except Exception:
    print("Você não digitou um número!")
    exit()
