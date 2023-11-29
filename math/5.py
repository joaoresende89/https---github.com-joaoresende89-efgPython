# programa que calcula a interseção de 3 ou mais conjuntos

i = int(input("Informe a quantidade de conjuntos: "))
j = int(input("Informe a quantidade de elementos: "))

matriz =[]

# FUNÇÃO PARA LER OS CONJUNTOS DENTRO DE UMA MATRIZ
def lerConjuntos(conj, coluna):
    matriz = []
    for i in range(conj):
        linha = []
        print(f"Informe os elementos do {i+1}º conjunto:")
        for j in range(coluna):
            list.append(linha, input())
        matriz = matriz + [linha]
    return matriz

# FUNÇÃO PARA CALCULAR A INTERSEÇÃO
def intersec(a, b):
    c = []
    for i in range(len(a)):
        if a[i] in b:
            c.append(a[i])
    return c

matriz = lerConjuntos(i,j)

print(matriz)

# pegar a quantidade de conjuntos dentro da matriz
quantConj = len(matriz)

if quantConj == 2:
    print(intersec(matriz[0], matriz[1]))
else:
    result = matriz[0]
    i = 1
    while i < (quantConj):
        result = intersec(result, matriz[i])
        i += 1
    print(result)
