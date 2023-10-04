# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
#  e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if media >= 9.0:
    print("Média de aproveitamento", media, "Conceito: A")
    print("Notas:", n1, "e", n2)
    print("APROVADO")
elif media >= 7.5 and media < 8.99:
    print("Média de aproveitamento", media, "Conceito: B")
    print("Notas:", n1, "e", n2)
    print("APROVADO")
elif media >= 6.0 and media < 7.49:
    print("Média de aproveitamento", media, "Conceito: C")
    print("Notas:", n1, "e", n2)
    print("APROVADO")
elif media >= 4.0 and media < 5.99:
    print("Média de aproveitamento", media, "Conceito: D")
    print("Notas:", n1, "e", n2)
    print("REPROVADO")
elif media == 0.0 and media < 3.99:
    print("Média de aproveitamento", media, "Conceito: C")
    print("Notas:", n1, "e", n2)
    print("REPROVADO")

