# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Informe um número inteiro: "))

if num < 1:
    print(f"{num} não é primo.")
    exit()

i = 2

while i < num:
    if num % i == 0 :
        print(f"{num} não é primo.")
        exit()
    else:
        i += 1

print(f"{num} é primo.")

