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
# FUNÇÃO PARA CALCULAR A UNIÃO DE TRÊS CONJUNTOS
def uniao(a, b, c):
    d = a
    for i in range(0,len(b)):
        if b[i] not in a:
            d.append(b[i])
    e = d
    for i in range(0,len(c)):
        if c[i] not in d:
            e.append(c[i])
    return e

# FUNÇÃO PARA CALCULAR A INTERSEÇÃO DE TRÊS CONJUNTOS

def intersec(a, b ,c):
    d = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                d.append(b[j])
                j = len(b)
    e = []
    for i in range(len(d)):
        for j in range(len(c)):
            if d[i] == c[j]:
                e.append(c[j])
                j = len(c)
    return e

# def intersec(a, b, c):
#     d = []
#     for i in range(0,len(a)):
#         if a[i] in b:
#             d.append(a[i])
#     print(d)
#     e = []
#     for i in range(0,len(d)):
#         if d[i] in c:
#             e.append(d[i])
#     return e

# def intersec(a,b):
#     c = []
#     for i in range(0,len(a)):
#         if a[i] in b:
#             c.append(a[i])
#     return c

# FUNÇÃO QUE MOSTRA A DIFERENÇA ENTRE TRÊS CONJUNTOS
def diferenca(a, b, c):
    d = []
    for i in range(len(a)):
        if a[i] not in b:
            d.append(a[i])
    e = []
    for i in range(len(d)):
        if d[i] not in c:
            e.append(d[i])
    return e

# FUNÇÃO PARA CALCULAR O COMPLEMENTO DOS TRÊS CONJUNTOS
def complemento(a, b, c):
    d = []
    for i in range(len(b)):
        if b[i] not in a:
            d.append(b[i])
    e = []
    for i in range(len(c)):
        if c[i] not in d:
            e.append(c[i])
    return e

print(A)
print(B)
print(C)

print(uniao(A, B, C))
print(intersec(A, B, C))
print(diferenca(A, B, C))
print(complemento(A, B, C))

