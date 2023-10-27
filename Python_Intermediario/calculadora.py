# Fazer uma calculadora, operações simples + - / * e tratar erros como divisão por zero

def soma(a, b):
    a = float(a)
    b = float(b)
    return a + b

def subtracao(a, b):
    a = float(a)
    b = float(b)
    return a - b

def multiplicacao(a, b):
    a = float(a)
    b = float(b)
    return a * b

def divisao(a, b) :
    a = float(a)
    b = float(b)
    if b == 0 or a == 0:
        return "Não é possível dividir por zero"
    else:
        return a / b

opcao = 1

while opcao != 0:
    print('''
++++++++++++++++++++++++++++++++
+ CALCULADORA DE DOIS NÚMEROS  +
++++++++++++++++++++++++++++++++
+ ESCOLHA QUAL OPERAÇÂO DESEJA +
+ 1 - SOMA                     +
+ 2 - SUBTRAÇÃO                +
+ 3 - MILTIPLICAÇÃO            +
+ 4 - DIVISÃO                  +
++++++++++++++++++++++++++++++++
Para sair digite 0
          ''')
    
    opcao = int(input("\nInforme uma opção: "))

    if opcao == 0:
        exit()
    if opcao > 4:
        print("Opção inválida!")
    else:
        a = input("Informe o primeiro número: ")
        b = input("Informe o segundo número: ")

        if a.isalpha() or b.isalpha():
            print("Número(s) inválido(s)!")
        else:
            if opcao == 1:
                print(f"\nO resultado é: {soma(a,b)}")
            elif opcao == 2:
                print(f"\nO resultado é: {subtracao(a,b)}")
            elif opcao == 3:
                print(f"\nO resultado é: {multiplicacao(a,b)}")
            elif opcao == 4:
                print(f"\nO resultado é: {divisao(a,b)}")

