# receber dois conjuntos e retornar um novo conjunto contendo a diferença entre eles

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

C = []

for k in range(0,i):
    if A[k] not in B:
        C.append(A[k])

print("O conjunto da diferença entre A e B é:",C)