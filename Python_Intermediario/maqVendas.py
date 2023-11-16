# troco com o menor número possível de moedas, entrar com um valor do produto e depois com o valor dado
# troco só em moedas

produto = float(input("Informe o valor do produto: "))

valorInserido = 0
while valorInserido <= produto:
    valorInserido = float(input("Insira o valor que você vai pagar: "))
    if valorInserido < produto:
        print("Valor incorreto, informe novamente!")


troco = valorInserido - produto

# print(troco)

# if troco <= 0:
#     print("Valor inserido insuficiente! Insira mais dinheiro!")
#     valorInserido = valorInserido + float(input("Insira mais dinheiro: "))

umReal = 0
cinquenta = 0
vinteEcinco = 0
dez = 0
cinco = 0
um = 0

print("Seu troco será de R$",troco)

while troco >= 1:
    troco = troco - 1
    umReal += 1

while troco >= 0.50:
    troco = troco - 0.50
    cinquenta += 1

troco = round(troco, 2)

while troco >= 0.25:
    troco = troco - 0.25
    vinteEcinco += 1

troco = round(troco, 2)

while troco >= 0.10:
    troco = troco - 0.10
    dez += 1

troco = round(troco, 2)

while troco >= 0.05:
    troco = troco - 0.05
    cinco += 1

troco = round(troco, 2)

while troco > 0:
    troco = troco - 0.01
    um += 1


print("E terá",umReal+cinquenta+vinteEcinco+dez+cinco+um,"moedas, sendo elas:")
print(umReal,"de 1 real")
print(cinquenta,"de 0,50")
print(vinteEcinco,"de 0,25")
print(dez,"de 0,10")
print(cinco,"de 0,05")
print(um,"de 0,01")


