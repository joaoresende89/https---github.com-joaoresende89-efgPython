# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

aluno = []
alturaAluno = []

for i in range(0,10):
    aluno.append(int(input("Informe o número do aluno: ")))
    alturaAluno.append(int(input("Informe a altura do aluno (cm): ")))

maisAlto = alturaAluno.index(max(alturaAluno))
maisBaixo = alturaAluno.index(min(alturaAluno))

print(f"O aluno mais alto é o de código: {aluno[maisAlto]}, com a altura de {alturaAluno[maisAlto]} cm")
print(f"O aluno mais baixo é o de código: {aluno[maisBaixo]}, com a altura de {alturaAluno[maisBaixo]} cm")

