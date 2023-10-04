# programa que lê tres números e mostra-os em ordem crescente

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if n1 > n3:
    n1, n3 = n3, n1
if n1 > n2:
    n1, n2 = n2, n1
if n2 > n3:
    n2, n3 = n3, n2

print("A ordem crescente é: ", n1, n2, n3)

