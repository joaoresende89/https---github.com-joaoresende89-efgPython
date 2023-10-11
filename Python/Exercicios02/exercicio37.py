# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
# a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
# sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes


cliente = []
altura = []
peso =[]

i = 0

while True:
    cliente.append(int(input("informe o código do cliente: ")))
    # print(cliente[i])
    if cliente[i] != 0:
        altura.append(int(input("Informe sua altura (cm): ")))
        peso.append(float(input("Informe seu peso (kg): ")))
        i += 1
    else:
        break

codAlto = altura.index(max(altura))
codBaixo = altura.index(min(altura))
codGordo = peso.index(max(peso))
codMagro = peso.index(min(peso))

print("Dados do cliente mais alto")
print(f"Código: {cliente[codAlto]}")
print(f"Altura: {altura[codAlto]} cm")
print(f"Peso: {peso[codAlto]} kg")

print("Dados do cliente mais baixo")
print(f"Código: {cliente[codBaixo]}")
print(f"Altura: {altura[codBaixo]} cm")
print(f"Peso: {peso[codBaixo]} kg")

print("Dados do cliente mais gordo")
print(f"Código: {cliente[codGordo]}")
print(f"Altura: {altura[codGordo]} cm")
print(f"Peso: {peso[codGordo]} kg")

print("Dados do cliente mais magro")
print(f"Código: {cliente[codMagro]}")
print(f"Altura: {altura[codMagro]} cm")
print(f"Peso: {peso[codMagro]} kg")

print(f"Média de altura dos clientes: {((sum(altura))/len(altura)):.1f} cm")
print(f"Média do peso dos clientes: {((sum(peso))/len(peso)):.1f} kg")

# while True:
#     cliente[i] = input("Informe seu código: ")
#     if cliente[i] == 0:
#         break
#     else:
#         altura[i] = input("Informe sua altura: ")
#         peso[i] = input("Informe seu peso: ")
#         i += 1

# print(cliente[0])

