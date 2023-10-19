# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

A = int(input("Informe o valor de A: "))

if A == 0:
    print("A equação não é de segundo grau!")
    exit()

B = int(input("Informe o valor de B: "))
C = int(input("Informe o valor de C: "))

Delta = (B * B) - (4 * A * C)
#Delta = Delta ** (1/2)

print(Delta)

if Delta < 0:
    print("A equação não possui raízes reais!")
    exit()

if Delta == 0:
    raiz = -(B) / (2 * A)
    print("A equação possui apenas uma raíz real: ", raiz)
    exit()

raiz1 = (-(B) + Delta) / (2 * A)

raiz2 = (-(B) - Delta) / (2 * A)

print("A equação possui duas raízes reais, são elas: ", raiz1, "e ", raiz2)








