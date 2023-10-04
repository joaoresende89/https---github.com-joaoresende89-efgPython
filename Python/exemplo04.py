# vefica se o número de entrada fica entre 1 e 20 e se é par ou ímpar

# para converter a variável em int
# numero = int(numero) 
#


numero = int(input("Informe um número entre 1 e 20: "))

if numero < 1 or numero > 20:
    print("Valor incorreto!")
else:
    if numero % 2 == 0:
        print("O número", numero,"é par!")
    else:
        print("O número", numero,"é ímpar!")

