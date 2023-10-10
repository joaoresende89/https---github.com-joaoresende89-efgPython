# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Informe a quantidade de números: "))

conj = list(range(0,n))

for i in range(0,n):
    conj[i] = int(input(f"Informe o {i+1}° número: "))

print(f"O maior valor é {max(conj)}")

print(f"O menor valor é {min(conj)}")

print(f"A soma dos valores é igual a {sum(conj)}")


