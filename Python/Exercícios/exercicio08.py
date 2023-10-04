# pegar o preço de três produtos e mostrar qual o mais barato

n1 = float(input("Informe o primeiro preço: "))
n2 = float(input("Informe o segundo preço: "))
n3 = float(input("Informe o terceiro preço: "))


if n1 < n2:
    barato = n1
else:
    barato = n2
if n3 < barato:
    barato = n3

print("O menor valor é: ", barato)

