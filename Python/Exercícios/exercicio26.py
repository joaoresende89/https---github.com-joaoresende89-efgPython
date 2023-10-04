# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combistivel = input("Informe o tipo de combustível: ")
litro = float(input("Informe a quantidade de litos: "))

if combistivel.lower() == 'alcool' and litro > 0:
    if litro <= 20:
        valor = (litro * 1.9) - ((litro * 1.9) * 0.03)
        print(f"Valor a pagar: R${valor:.2f}")
    else:
        valor = (litro * 1.9) - ((litro * 1.9) * 0.05)
        print(f"Valor a pagar: R${valor:.2f}")
elif combistivel.lower() == 'gasolina'and litro > 0:
    if litro <= 20:
        valor = (litro * 2.5) - ((litro * 2.5) * 0.04)
        print(f"Valor a pagar: R${valor:.2f}")
    else:
        valor = (litro * 2.5) - ((litro * 2.5) * 0.06)
        print(f"Valor a pagar: R${valor:.2f}")
else:
    print("Não trabalhamos com o combustível indicado ou quantidade de litros inválida!")
