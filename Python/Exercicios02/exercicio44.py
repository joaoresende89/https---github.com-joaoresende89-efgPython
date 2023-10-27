# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
# (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
# Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']


num = []
par = []
impar = []

for i in range(5):
    num.append(int(input("Informe um número: ")))

for i in range(5):
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])
    
if len(par) > 0:
    print(f"Estes são os números pares: {par}")
else:
    print("Não há numeros pares")

if len(impar) > 0:
    print(f"Estes são os números impares: {impar}")
else:
    print("Nada de numeros impares")

