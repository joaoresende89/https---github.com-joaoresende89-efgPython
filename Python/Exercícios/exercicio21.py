# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input("Informe o valor a ser sacado: "))

if valor < 10 and valor > 600:
    print("Valor inválido!")
    exit()

nota_100 = 0
nota_50 = 0
nota_10 = 0
nota_5 = 0
nota_1 = 0

while valor > 0:
    if valor >= 100:
        nota_100 = nota_100 + 1
        valor = valor - 100
    elif valor >= 50:
        nota_50 = nota_50 + 1
        valor = valor - 50
    elif valor >= 10:
        nota_10 = nota_10 + 1
        valor = valor - 10
    elif valor >= 5:
        nota_5 = nota_5 + 1
        valor = valor - 5
    elif valor >= 1:
        nota_1 = nota_1 + 1
        valor = valor - 1

print("Nota de 100: ",nota_100)
print("Nota de 50: ",nota_50)
print("Nota de 10: ",nota_10)
print("Nota de 5: ",nota_5)
print("Nota de 1: ",nota_1)
