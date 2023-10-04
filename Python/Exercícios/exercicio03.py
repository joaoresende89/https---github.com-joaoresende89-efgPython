# programa que verifica se uma letra digitada é F ou M, conforme a letra escrever: F - Feminino, M - Masculino ou sexo inválido

sex = input("Digite sua sexualidade (M - Masculino, F - Feminino ou N - Não desejo informar): ")

if sex == "M":
    print("Masculino")
elif sex == "F":
    print("Feminino")
elif sex == "N":
    print("Sexo não informado")
else:
    print("Sexo inválido!")
    