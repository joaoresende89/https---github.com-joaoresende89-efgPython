# Criar um menu para mostrar as f3unções disponíveis para o usuário selecionar a função que ele quer executar

def verifica_primo():
    num = int(input("Informe um número inteiro: "))
    primo = 1
    if num <= 2:
        primo = 1
    i = 2
    while i < num:
        if num % i == 0:
            primo = 0
        i += 1    
    if primo == 1:
        print(f"{num} é primo!")
    else:
        print(f"{num} não é primo!")

def potencia():
    print("Programa que calula potência!")
    base = int(input("Informe a base: "))
    exp = int(input("Informe o expoente: "))
    result = 1
    for i in range(0,exp):
        result = result * base
    print(f"O resultado de {base} sobre {exp} é: {result}")

def fatorial():
    num = int(input("Informe o valor a ser calculado o fatorial: "))
    fat = 1
    print(f"{num}! = {num} .", end=" ")
    while num > 0:
        fat = fat * num
        num -= 1
        if num > 1:
            print(num,". ", end="")
        elif num == 1:
            print(num, end="")
    print(" =",fat)

def tabuada():
    num = int(input("Informe qual tabuada você quer calcular (1 a 10): "))
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")

def par_impar():
    num = int(input("Informe um número inteiro: "))
    if num % 2 == 0:
        print(f"{num} é par!")
    else:
        print(f"{num} é ímpar!")

def inverter():
    num = input("Informe um número inteiro positivo: ")
    if num < '0':
        print("Valor não válido!")
        exit()
    n = len(num)
    print("=>", end=" ")
    while n > 0:
        print(num[n-1], end="")
        n -= 1
    print("")

def raizes():
    A = int(input("Informe o valor de A: "))
    if A == 0:
        print("A equação não é de segundo grau!")
        exit()
    B = int(input("Informe o valor de B: "))
    C = int(input("Informe o valor de C: "))
    Delta = (B * B) - (4 * A * C)
    Delta = Delta ** (1/2)
    print(Delta)
    if Delta < 0:
        print("A equação não possui raízes reais!")
        exit()
    if Delta == 0:
        raiz = -(B) / (2 * A)
        print("A equação possui apenas uma raíz real: ", raiz)
        exit()
    raiz1 = (-(B) + Delta) / (2 * A)
    raiz2 = (-(B) - Delta) / (2 * A)
    print("A equação possui duas raízes reais, são elas: ", raiz1, "e ", raiz2)

def iR():
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

def reajuste():
    salario = float(input("Informe o salário em reais: "))
    if salario <= 280:
        salarioAnt = salario
        reajuste = 0.2
        aumento = salario * reajuste
        salario = salario + aumento
        print("Salário antes do reajuste: R$ ", salarioAnt,"\nPercentual de aumento aplicado: ", reajuste * 100, "%","\nValor do aumento: R$", aumento,
            "\nSalário após o aumento: R$", salario)
    elif salario > 280 and salario <= 700:
        salarioAnt = salario
        reajuste = 0.15
        aumento = salario * reajuste
        salario = salario + aumento
        print("Salário antes do reajuste: R$ ", salarioAnt,"\nPercentual de aumento aplicado: ", reajuste * 100, "%","\nValor do aumento: R$", aumento,
            "\n", "Salário após o aumento: R$", salario)
    elif salario > 700 and salario <= 1500:
        salarioAnt = salario
        reajuste = 0.1
        aumento = salario * reajuste
        salario = salario + aumento
        print("Salário antes do reajuste: R$ ", salarioAnt,"\nPercentual de aumento aplicado: ", reajuste * 100, "%","\nValor do aumento: R$", aumento,
            "\nSalário após o aumento: R$", salario)
    elif salario > 1500:
        salarioAnt = salario
        reajuste = 0.05
        aumento = salario * reajuste
        salario = salario + aumento
        print("Salário antes do reajuste: R$ ", salarioAnt,"\nPercentual de aumento aplicado: ", reajuste * 100, "%","\nValor do aumento: R$", aumento,
            "\nSalário após o aumento: R$", salario)

def combustivel():
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

# Criar um menu para mostrar as funções disponíveis para o usuário selecionar a função que ele quer executar

def menu():
    opcao = 1
    while opcao != 0:
        print('''
        ----------SEJA BEM VINDO AO SUPER MENU----------
        |       Escolha uma opção abaixo:              |
        |   1 - Verificar se um número é primo         |
        |   2 - Calcular potencia                      |
        |   3 - Calcular o fatorial de um número       |
        |   4 - Gerar a tabuada de um número           |
        |   5 - Verificar se um número é par ou ímpar  |
        |   6 - Inverter numero informado              |
        |   7 - Calcular as raízes da equação          |
        |   8 - Cálculo IR                             |
        |   9 - Reajuste salário                       |
        |  10 - Cálculo do combustível                 |
        |______________________________________________|
        ''')

        opcao = int(input("Digite uma das opções ou 0 para sair: "))

        if opcao == 1:
            verifica_primo()
        elif opcao == 2:
            potencia()
        elif opcao == 3:
            fatorial()
        elif opcao == 4:
            tabuada()
        elif opcao == 5:
            par_impar()
        elif opcao == 6:
            inverter()
        elif opcao == 7:
            raizes()
        elif opcao == 8:
            iR()
        elif opcao == 9:
            reajuste()
        elif opcao == 10:
            combustivel()
        else:
            print("Opção inválida!")

menu()



