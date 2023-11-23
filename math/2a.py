# C = [1, 2, 3, 4, 5]
# D = [4, 5, 6, 7, 8]

C = [1, 2, 3, 4, 5]
D = [4, 5, 6, 7, 8]

E = C

for i in range(0,5):
    if D[i] not in C:
        E.append(D[i])

print(E)