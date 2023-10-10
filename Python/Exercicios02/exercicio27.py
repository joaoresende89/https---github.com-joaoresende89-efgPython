# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turma = int(input("Informe a quantidade de turmas: "))
soma = 0

for i in range(0,turma):
    alunos = int(input(f"Informe a quantidade de alunos da turma {i}: "))
    if alunos > 40:
        alunos = int(input("A quantidade de alunos não pode ser maior que 40, informa a quantidade novamente: "))
    soma = soma + alunos

print(f"A quantidade média de alunos por turma é de {soma/turma:.1f} alunos")


