# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = list(range(5))

for i in range(0,5):
    numeros[i] = int(input(f"Informe o {i+1}° número: "))

print(f"A soma dos números é igual a: {sum(numeros)}")
print(f"A média dos números é igual a: {sum(numeros)/5}")

