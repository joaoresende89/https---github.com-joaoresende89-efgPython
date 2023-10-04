# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe seu nome: ")

while len(nome) < 4:
    print("Valor inválido!")
    nome = input("Informe um nome maior que 3 caracteres: ")

idade = int(input("Informe sua idade: "))

while idade < 0 or idade > 150:
    print("Valor inválido!")
    idade = int(input("Informe idade maior que 0 e menor que 150: "))

salario = float(input("Informe seu salário: "))

while salario <= 0:
    print("Valor inválido!0")
    salario = float(input("Informe seu salário (maior que zero): "))

sexo = input("Informe seu sexo (M/F): ")

while sexo.lower() != 'm' and sexo.lower() != 'f':
    print("Valor inválido!")
    sexo = input("Informe o sexo, M - Masculino e F - Feminino: ")

estadoCivil = input("Informe seu estado civil: ")

estadoCivil_list = ['s', 'c', 'v', 'd']

while estadoCivil.lower() not in estadoCivil_list:
    estadoCivil = input("Estado civil inválido! Digite novamente:")

print("Dados corretos!")


