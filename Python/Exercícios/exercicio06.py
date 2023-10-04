# programa que receba 3 números e apresente o maior

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

maior = 0

if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3

print("O número maior é: ", maior)

