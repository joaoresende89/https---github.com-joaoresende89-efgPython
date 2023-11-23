# C = [1, 2, 3, 4, 5]
# D = [4, 5, 6, 7, 8]

D = [4, 5, 6, 7, 8]
U = [1, 2, 3, 4, 5, 6, 7, 8, 9]

R = []

for i in range(0,9):
    if U[i] not in D:
        R.append(U[i])
    
print(R)