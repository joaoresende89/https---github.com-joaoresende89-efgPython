# A = {"a", "b", "c", "d"}
# B = {"c", "d", "e", "f"}
# a- calcular a união de A e B e imprimir o resultado
# b- calcular a inteseção de A e B


A = ["a", "b", "c", "d"]
B = ["c", "d", "e", "f"]

C = A

for i in range(0,4):
    if B[i] not in A:
        C.append(B[i])

print(C)


