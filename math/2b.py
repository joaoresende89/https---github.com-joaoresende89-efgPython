# C = [1, 2, 3, 4, 5]
# D = [4, 5, 6, 7, 8]

C = [1, 2, 3, 4, 5]
D = [4, 5, 6, 7, 8]

E = []

for i in range(0,5):
    for j in range(0,5):
        if C[i] == D[j]:
            E.append(D[j])
            j = 4

print(E)

