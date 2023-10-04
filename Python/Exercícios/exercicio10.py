# programa que lê o turno m-matutino, v-vespertino e n-noturno e imprime a mensagem bom dia, boa tarde ou boa noite.

turno = input("Informe o turno (M-Matutino, V-Vespertino ou N-Noturno): ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

