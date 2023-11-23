# A = {"a", "b", "c", "d"}
# B = {"c", "d", "e", "f"}
# a- calcular a união de A e B e imprimir o resultado
# b- calcular a inteseção de A e B


A = ["a", "b", "c", "d"]
B = ["c", "d", "e", "f"]

C = []

for i in range(0,4):
    for j in range(0,4):
        if A[i] == B[j]:
            C.append(B[j])
            j = 4

print(C)
