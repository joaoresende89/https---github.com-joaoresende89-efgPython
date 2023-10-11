# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salarioInic = 1000
percentual = 0.015
ano = 1995

while ano <= 2023:
    salario = salarioInic + (salarioInic * percentual)
    percentual = percentual * 2
    ano += 1
    # print(percentual)
    # print(f"{salario:.2f}")

print(f"O salário atual é de R$ {salario:.2f}")

salarioInic = int(input("Informe o salario inicial: "))
ano = int(input("Informe o ano inicial: "))
percentual = 0.015
salario = 0

while ano <= 2023:
    salario = salarioInic + (salarioInic * percentual)
    percentual = percentual * 2
    ano += 1

print(f"O salário atual é de R$ {salario:.2f}")



