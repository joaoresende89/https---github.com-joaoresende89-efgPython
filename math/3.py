# A = [2, 3, 1, 4, 5, 6]
# B = [2, 3, 1, 7, 8, 5, 6, 4]

A = [2, 3, 1, 4, 5, 6]
B = [2, 3, 1, 7, 8, 5, 6, 4]

C = []

for i in range(0,6):
    for j in range(0,8):
        if A[i] == B[j]:
            C.append(A[i])
            j = 8

print("A =",A)
print("B =",B)
if C == A:
    print("A é subconjunto de B:",C)
else:
    print("A não é subconjunto de B!")