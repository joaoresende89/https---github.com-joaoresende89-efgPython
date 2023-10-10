# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

i = 0

while i == 0:
    num = int(input("Informe um número inteiro menor que 16: "))
    if num < 16:
        i += 1
    else:
        print("Número fora do intervalo, informe novamente.")

fat = 1

while num > 0:
    fat = fat * num
    num -= 1

print(fat)

