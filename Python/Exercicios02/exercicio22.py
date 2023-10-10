# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Informe um número inteiro: "))

if num < 1:
    print(f"{num} não é primo.")
    exit()

i = 2

primo = 0

while i < num:
    if num % i == 0 :
        print(f"{num} é divisível por {i}")
        primo = 1
    i += 1

if primo == 1:
    print(f"{num} não é prmimo.")
else:
    print(f"{num} é primo.")
