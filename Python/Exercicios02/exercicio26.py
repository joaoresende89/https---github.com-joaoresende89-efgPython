# Numa eleição existem três candidatos.
# Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitor = int(input("Informe a quantidade de eleitores: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0
nuloBranco = 0

print("*******************ELEIÇÕES*********************")
print("******************CANDIDATOS********************")
print("* Zezinho Fernandes - n° 10                    *")
print("* Chico da Costa    - n° 69                    *")
print("* Tonho do Caminhão - n° 74                    *")
print("************************************************")

for i in range(0,eleitor):
    voto = input(f"Eleitor {i+1}, informe seu voto: ")
    if voto == '10':
        candidato1 += 1
    elif voto == '69':
        candidato2 += 1
    elif voto == '74':
        candidato3 += 1
    else:
        nuloBranco += 1

print("*******************ELEIÇÕES*********************")
print("******************RESULTADO*********************")
print(f"* Zezinho Fernandes - {candidato1} votos                  *")
print(f"* Chico da Costa    - {candidato1} votos                  *")
print(f"* Tonho do Caminhão - {candidato1} votos                  *")
print(f"* Brancos/Nulos     - {nuloBranco} votos                  *")
print("************************************************")


