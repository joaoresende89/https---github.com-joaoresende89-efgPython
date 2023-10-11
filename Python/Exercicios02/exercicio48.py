# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489
#   => 98467321

num = input("Informe um número inteiro positivo: ")

if num < '0':
    print("Valor não válido!")
    exit()

n = len(num)

while n > 0:
    print(num[n-1], end="")
    n -= 1

