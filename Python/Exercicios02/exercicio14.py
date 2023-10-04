# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = list(range(10))

for i in range(0,10):
    numeros[i] = int(input(f"Informe o {i+1}° número: "))

par = 0
impar = 0

for i in range(0,10):
    if numeros[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"A quantodade de números páres é: {par}")
print(f"A quantodade de números ímpares é: {impar}")

