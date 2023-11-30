# programa que calcula a interseção de 3 ou mais conjuntos

# FUNÇÃO LÊ OS ELEMENTOS DO CONJUNTO E PEDE A QUANTIDADE DE ELEMENTOS QUE O CONJUNTO TERÁ
def leConj(i):
    a = []
    quant = int(input(f"Informe a quantidade de elementos do {i+1}° conjunto: "))
    for i in range(quant):
        a.append(input())
    return a

# FUNÇÃO PARA CALCULAR A INTERSEÇÃO
def intersec(a, b):
    c = []
    for i in range(len(a)):
        if a[i] in b:
            c.append(a[i])
    return c

# INICIO DO PROGRAMA
conj = int(input("Informe a quantidade de conjuntos: "))

matriz = []

for i in range(conj):
    matriz.append(leConj(i))

print(matriz)

if conj < 2:
    print("Não tem como fazer a intersecção só de um conjunto, não é mesmo?!")
elif conj == 2:
    print(intersec(matriz[0], matriz[1]))
else:
    result = matriz[0]
    i = 1
    while i < (conj):
        result = intersec(result, matriz[i])
        i += 1
    print(result)

