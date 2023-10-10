# Faça um programa que calcule o mostre a média aritmética de N notas.

quant = int(input("informe a quantidade de notas: "))

soma = 0

for i in range(0,quant):
    nota = float(input(f"Informe a {i+1}° nota: "))
    soma = soma + nota

print(f"A média aritimética das {quant} notas é igual a {(soma/quant):.1f}")

