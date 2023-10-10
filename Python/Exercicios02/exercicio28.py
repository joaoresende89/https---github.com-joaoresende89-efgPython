# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

cds = int(input("Informe a quantidade de CDs: "))

soma = 0

for i in range(cds):
    valor = float(input(f"Informe o valor do {i+1}° CD: "))
    soma = soma + valor

print(f"O valor médio de cada CD é R$ {soma/cds:.2f}")

