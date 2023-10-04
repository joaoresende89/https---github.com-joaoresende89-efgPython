# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

maca = float(input("Informe a quantidade de maçãs (Kg): "))
morango = float(input("Informe a quantidade de morangos (Kg): "))

valorTotal = 0
valorMaca = 0
valorMorango = 0

if maca <= 5:
    valorMaca = maca * 2.5
else:
    valorMaca =  maca * 2.2

if morango <= 5:
    valorMorango = morango * 1.8
else:
    valorMorango = morango * 1.5

valorTotal = valorMaca + valorMorango

if (maca + morango) > 8:
    valorTotal = valorTotal - (valorTotal * 0.1)

print(f"Valor a ser pago R${valorTotal:.2f}")

