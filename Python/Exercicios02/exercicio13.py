# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

print("Programa que calula potência!")
base = int(input("Informe a base: "))
exp = int(input("Informe o expoente: "))
result = 1

for i in range(0,exp):
    result = result * base

print(result)


