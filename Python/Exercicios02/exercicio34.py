# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
# Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input("Informe um número inteiro: "))

primo = 1

if num <= 2:
    primo = 1

i = 2
while i < num:
    if num % i == 0:
        primo = 0
    i += 1
    
if primo == 1:
    print(f"{num} é primo!")
else:
    print(f"{num} não é primo!")