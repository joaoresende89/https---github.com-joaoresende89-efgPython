# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

cont = 1

paisA = 80000
paisB = 200000

while cont > 0:
    taxaA = input("Informe a taxa de crescimento do país com 80000 habitantes em porcentagem: ")
    taxaB = input("Informa a taxa de crescimento do país com 200000 habitantes em porcentagem: ")
    if taxaA <= taxaB:
        print("Informe valores válidos! Taxa de crescimento do país com 80000 habitantes tem que ser maior do que a taxa do país com 200000 habitantes.")
        cont += 1
    else:
        taxaA = float(taxaA)
        taxaB = float(taxaB)
        ano = 0
        while paisA < paisB:
            paisA = paisA + (paisA * (taxaA/100))
            paisB = paisB + (paisB * (taxaB/100))
            ano += 1
        cont = 0

print(f"A quantidade foi de {ano} anos.")

