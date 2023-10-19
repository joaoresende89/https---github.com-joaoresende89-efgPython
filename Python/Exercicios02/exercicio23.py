# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
# Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input("Informe um número inteiro: "))
cont = 0

for i in range(1, numero+1):

    primo = 1
    if i <= 2:
        primo = 1
    j = 2
    while j < i:
        if i % j == 0:
            primo = 0
        j += 1    
    if primo == 1:
        print(i)
        cont += 1
  
print(f"Quantidade de divisões: {cont}")
