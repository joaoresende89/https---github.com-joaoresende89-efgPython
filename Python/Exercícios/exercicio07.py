# programa que lê tres numeros e mostre o menor e o maior deles

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

maior = 0
menor = 0

if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3

if n1 < n2:
    menor = n1
else:
    menor = n2
if n3 < menor:
    menor = n3

print("O número maior é: ", maior)
print("O número menor é: ", menor)
