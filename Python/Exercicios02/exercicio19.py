# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Informe a quantidade de números: "))

conj = list(range(0,n))

for i in range(0,n):
    conj[i] = int(input(f"Informe o {i+1}° número: "))
    if conj[i] > 1000:
        print("Número fora do padrão, informe novamente.")
        conj[i] = int(input(f"Informe o {i+1}° número: "))

print(f"O maior valor é {max(conj)}")

print(f"O menor valor é {min(conj)}")

print(f"A soma dos valores é igual a {sum(conj)}")

