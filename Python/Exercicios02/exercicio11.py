# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

soma = 0

if n1 < n2:
    for i in range(n1+1, n2):
        soma = soma + i
    print(f"A soma do intervalo é: {soma}")
else:
    for i in range(n2+1, n1):
        soma = soma + i
    print(f"A soma do intervalo é: {soma}")

