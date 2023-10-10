# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Informe um número inteiro: "))

primos = []

for n in range(1, num+1):
    primo = 1

    if num <= 2:
        primo = 1

    i = 2
    while i < n:
        if n % i == 0:
            primo = 0
        i += 1
    
    if primo == 1:
        primos.append(n)

print(primos)