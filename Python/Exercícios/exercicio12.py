# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
# e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao 
# Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

horaValor = int(input("Informe o valor da sua hora: "))
horaQuant = int(input("Informe a quantidade de hora: "))

salarioBruto = horaQuant * horaValor

if salarioBruto <= 900:
    sindicato = salarioBruto * 0.03
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11
    totalDesc = sindicato + inss
    salarioLiq = salarioBruto - totalDesc
    print("Salário Bruto: ", "(",horaValor,"*",horaQuant,") : R$ ", salarioBruto)
    print("(-) Sindicado (3%)                               : R$ ", sindicato)
    print("(-) IR                                           : ISENTO")
    print("(-) INSS ( 10% )                                 : R$ ", inss)
    print("FGTS (11%)                                       : R$ ", fgts)
    print("Total de descontos                               : R$ ", totalDesc)
    print("Salário Liquido                                  : R$ ", salarioLiq)

elif salarioBruto > 901 and salarioBruto <= 1500:
    sindicato = salarioBruto * 0.03
    irrf = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11
    totalDesc = sindicato + inss + irrf
    salarioLiq = salarioBruto - totalDesc
    print("Salário Bruto: ", "(",horaValor,"*",horaQuant,") : R$ ", salarioBruto)
    print("(-) Sindicado (3%)                               : R$ ", sindicato)
    print("(-) IR (5%)                                      : R$ ", irrf)
    print("(-) INSS ( 10% )                                 : R$ ", inss)
    print("FGTS (11%)                                       : R$ ", fgts)
    print("Total de descontos                               : R$ ", totalDesc)
    print("Salário Liquido                                  : R$ ", salarioLiq)

elif salarioBruto > 1501 and salarioBruto <= 2500:
    sindicato = salarioBruto * 0.03
    irrf = salarioBruto * 0.1
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11
    totalDesc = sindicato + inss + irrf
    salarioLiq = salarioBruto - totalDesc
    print("Salário Bruto: ", "(",horaValor,"*",horaQuant,") : R$ ", salarioBruto)
    print("(-) Sindicado (3%)                               : R$ ", sindicato)
    print("(-) IR (10%)                                     : R$ ", irrf)
    print("(-) INSS ( 10% )                                 : R$ ", inss)
    print("FGTS (11%)                                       : R$ ", fgts)
    print("Total de descontos                               : R$ ", totalDesc)
    print("Salário Liquido                                  : R$ ", salarioLiq)

elif salarioBruto > 2501:
    sindicato = salarioBruto * 0.03
    irrf = salarioBruto * 0.2
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11
    totalDesc = sindicato + inss + irrf
    salarioLiq = salarioBruto - totalDesc
    print("Salário Bruto: ", "(",horaValor,"*",horaQuant,") : R$ ", salarioBruto)
    print("(-) Sindicado (3%)                               : R$ ", sindicato)
    print("(-) IR (10%)                                     : R$ ", irrf)
    print("(-) INSS ( 10% )                                 : R$ ", inss)
    print("FGTS (11%)                                       : R$ ", fgts)
    print("Total de descontos                               : R$ ", totalDesc)
    print("Salário Liquido                                  : R$ ", salarioLiq)

else:
    exit()

