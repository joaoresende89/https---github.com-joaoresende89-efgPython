# recebe nome e idade, verifica se é maior ou menor de idade, se a idade é par ou ímpar e se pode votar

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

print("Nome:", nome, "\nIdade:", idade)

if int(idade) >= 18: 
    print("Você é adulto!!!")
else:
    print("Menor!!")

if int(idade) % 2 == 0:
    print("Sua idade é par!")
else:
    print("Sua idade é ímpar!")

if int(idade) >= 16 and int(idade) <= 18:
    print("Você já pode votar!")
elif int(idade) < 16 :
    print("Você não vota!")
elif int(idade) >= 70:
    print("Você não é obrigado a votar!")
else:
    print("Você é obrigado a votar!!!!")

