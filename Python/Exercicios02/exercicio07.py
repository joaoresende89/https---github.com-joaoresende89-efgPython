# Faça um programa que leia 5 números e informe o maior número.

# n1 = input("Informe o primeiro número: ")
# n2 = input("Informe o segundo número: ")
# n3 = input("Informe o terceiro número: ")
# n4 = input("Informe o quarto número: ")
# n5 = input("Informe o quinto número: ")

# cont = 0

# # while cont < 5:

# numeros = []*5

# while cont < 5:
#     numeros[cont] = input(f"Informe o {cont+1}° número: ")
#     cont += 1


# # numeros = input("informe um numero:"), input("informe outro numero:"), input("informe outro numero:")
           
# print(max(numeros))

numeros = list(range(5))

for i in range(0,5):
    numeros[i] = int(input(f"Informe o {i+1}° número: "))

print("O maior número é: ", max(numeros))