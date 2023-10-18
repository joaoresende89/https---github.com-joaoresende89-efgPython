# Criar um menu para mostrar as funções disponíveis para o usuário selecionar a função que ele quer executar

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

# Criar um menu para mostrar as funções disponíveis para o usuário selecionar a função que ele quer executar

def menu():
    opcao = 1
    while opcao != 0:
        print("-----Seja bem vindo ao Super Menu-----")
        print("Escolha uma opção abaixo:")
        print("1 - Verificar se um número é primo")
        print("2 - Calcular potencia")
        print("3 - Calcular o fatorial de um número")
        print("4 - Gerar a tabuada de um número")
        print("5 - Verificar se um número é par ou ímpar")
        print("6 - Inverter numero informado")

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
        else:
            print("Opção inválida!")

menu()



