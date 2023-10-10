# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("informe um número inteiro: "))

cont = 0
j = 2
primo = 0

for i in range(1,num+1):
    if i < 4:
        cont += 1
        print(i, cont)
    else:
        if i % j == 0:
            j += 1
        else:
            cont += 1
            primo = i
        print(primo, cont)