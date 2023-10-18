# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
# [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

controle = 0
grupo1 = []
grupo2 = []
grupo3 = []
grupo4 = []

while controle == 0:
    num = float(input("Infome um número positivo: "))

    if num >= 0 and num <= 25:
        grupo1.append(num)
    if num > 25 and num <= 50:
        grupo2.append(num)
    if num > 50 and num <= 75:
        grupo3.append(num)
    if num > 75 and num <= 100:
        grupo4.append(num)
    if num < 0:
        break

print(f"A quantidade de números entre [0-25] é: {len(grupo1)}")
print(f"A quantidade de números entre [26-50] é: {len(grupo2)}")
print(f"A quantidade de números entre [51-75] é: {len(grupo3)}")
print(f"A quantidade de números entre [76-100] é: {len(grupo4)}")
