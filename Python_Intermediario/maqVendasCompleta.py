# Considere o mesmo problema anterior e agora a regra inicial e a devolução
# de troco procura minimizar o máximo possível o número de notas e moedas
# para o usuário.
# Regra Inicial da Máquina, ela devolve o troco em moedas e notas de 2, 5, 10,
# 20 e 50 reais, e aceita moeda 1 real e notas de 2, 5, 10, 20, 50, 100 e 200
# reais.

produto = int(input("Informe o valor do produto: "))

deposito = 0
while deposito <= produto:
    deposito = int(input("Insira o valor que você vai pagar: "))
    if deposito < produto:
        print("Valor incorreto, informe novamente!")

troco = deposito - produto

print(f"Seu troco é: {troco}")

duzentos = troco // 200
troco %= 200

cem = troco // 100
troco %= 100

cinquenta = troco // 50
troco %= 50

vinte = troco // 20
troco %= 20

dez = troco // 10
troco %= 10

cinco = troco // 5
troco %= 5

dois = troco // 2
troco %= 2

um = troco // 1

print(f"{duzentos} notas de 200")
print(f"{cem} notas de 100")
print(f"{cinquenta} notas de 50")
print(f"{vinte} notas de 20")
print(f"{dez} notas de 10")
print(f"{cinco} notas de 5")
print(f"{dois} notas de 2")
print(f"{um} moedas de 1")
