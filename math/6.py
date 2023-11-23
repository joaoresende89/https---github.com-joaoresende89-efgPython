# programa que aceite três conjuntos A, B e U (universal) como entrada e calcule e imprima:
# união
# interseção
# diferença
# complemento

i = int(input("Quantos elementos terá o conjunto A? "))
print(f"Informe os {i} elementos do conjunto A: ")

A = []

for j in range(0,i):
    A.append(input())

j = int(input("Quantos elementos terá o conjunto B? "))
print(f"Informe os {j} elementos do conjunto B: ")

B = []

for j in range(0,j):
    B.append(input())

k = int(input("Quantos elementos terá o conjunto C? "))
print(f"Informe os {k} elementos do conjunto C: ")

C = []

for k in range(0,k):
    C.append(input())

# UNIAO - primeiro faz de dois conjuntos e depois com o outro
D = A

for i in range(0,j):
    if B[j] not in A:
        D.append(B[j])


