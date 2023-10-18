# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input("Qual o valor da dívida: "))

print("Valor da Dívida - Valor dos Juros - Quantidade de Parcelas - Valor da Parcela")
print(f"R${divida:9.2f}       0                 1                        R${divida:9.2f}")

juros = 0.1
valorParcela = 0

# o for começa em 3, o i vai incrementando 3 até 12
for i in range(3,13,3):
    print(f"R${divida+(divida*juros):9.2f}       {(divida*juros):.0f}               {i}                        R${(divida+(divida*juros))/i:9.2f}")
    juros = juros + 0.05
    
