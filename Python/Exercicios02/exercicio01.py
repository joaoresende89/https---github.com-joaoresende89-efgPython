# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# i = 1

# while i > 0:
#     nota = int(input("Informe uma nota entre 0 e 10: "))
#     if nota < 0 or nota > 10:
#         i =+ 1
#     else:
#         i =-1

# print(nota)

nota = int(input("Informe uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    nota = int(input("Informe um valor válido: "))

print(f"A nota é: {nota}")


