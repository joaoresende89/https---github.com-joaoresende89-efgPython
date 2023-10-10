# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Informe um número inteiro: "))

fat = 1

while num > 0:
    fat = fat * num
    num -= 1

print(fat)

