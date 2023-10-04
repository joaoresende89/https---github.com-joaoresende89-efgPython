# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num = int(input("Informe um valor inteiro menor que 1000: "))

if num > 1000 and num > 0:
    print("Valor inválido!")
    exit()

centena = (num // 100) % 10
dezena = (num % 100) // 10
unidade = (num % 100) % 10

if centena == 0 :
    if dezena == 0:
        if unidade <= 1:
            print(num,"=",unidade,"unidade")
        else:
            print(num,"=",unidade,"unidades")
    elif dezena == 1:
        if unidade <= 1:
            print(num,"=",dezena,"dezena e",unidade,"unidade")
        else:
            print(num,"=",dezena,"dezena e",unidade,"unidades")
    elif dezena > 1:
        if unidade <= 1:
            print(num,"=",dezena,"dezenas e",unidade,"unidade")
        else:
            print(num,"=",dezena,"dezenas e",unidade,"unidades")
elif centena == 1:
    if dezena == 1:
        if unidade <= 1:
            print(num,"=",centena,"centena,",dezena,"dezena e",unidade,"unidade")
        else:
            print(num,"=",centena,"centena,",dezena,"dezena e", unidade,"unidades")
    else:
        if unidade <= 1:
            print(num,"=",centena,"centena,",dezena,"dezenas e",unidade,"unidade")
        else:
            print(num,"=",centena,"centena, ",dezena,"dezenas e",unidade,"unidades")
else:
    if dezena == 1:
        if unidade <= 1:
            print(num,"=",centena,"centenas,",dezena,"dezena e",unidade,"unidade")
        else:
            print(num,"=",centena,"centenas,",dezena,"dezena e", unidade,"unidades")
    else:
        if unidade <= 1:
            print(num,"=",centena,"centenas,",dezena,"dezenas e",unidade,"unidade")
        else:
            print(num,"=",centena,"centenas, ",dezena,"dezenas e",unidade,"unidades")

