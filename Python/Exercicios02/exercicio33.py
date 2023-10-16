# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
# e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

# temp = input("Informe as temperaturas separadas por vígula: ")
i = 0
temp = []

while True:
    temp.append(input("Informe a temperatura: "))
    if temp[i] != '':
        i += 1
    else:
        break
    
print(f"A temperatura máxima é: {max(temp[:-1])}")
print(f"A temperatura mínima é: {min(temp[:-1])}")
newTemp = [float(string) for string in temp[:-1]]
print(f"A média de temperatura é: {(sum(newTemp))/i:.1f}")

# teste = temp.split(", ")

# print(temp)    



