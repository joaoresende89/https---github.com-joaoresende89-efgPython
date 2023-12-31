# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidade = []
veiculos = []
acidentes = []

for i in range(5):
    cidade.append(int(input("Informe o código da cidade: ")))
    veiculos.append(int(input("Informe o quantidade de veículos de passeio da cidade: ")))
    acidentes.append(int(input("Informe a quantidade de acidentes de trânsito com vítimas: ")))

maxAcidente = acidentes.index(max(acidentes))
minAcidentes = acidentes.index(min(acidentes))

print(f"A cidade com maior índice de acidentes de transito é a cidade {cidade[maxAcidente]}, com o número de {acidentes[maxAcidente]} acidentes.")
print(f"A cidade com menor índice de acidentes de transito é a cidade {cidade[minAcidentes]}, com o número de {acidentes[minAcidentes]} acidentes.")
print(f"A média de veículos das cidades é de {(sum(veiculos))/5:.1f}")

medAcidente = 0
cont = 0

for i in range(5):
    if cidade[i] < 2000:
        medAcidente = medAcidente + acidentes[i]
        cont += 1

print(f"A média de acidentes em cidade com mais de 2000 carros é de {medAcidente/cont}")


