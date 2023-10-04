# progrma que faz a média de duas notas e apresente a mensagem se aprovado (maior ou igual a média), 
# reprovado (média menor que 7) ou aprovado com distinção se a média for igual a dez

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))

# nota1 = int(nota1)
# nota2 = int(nota2)

media = (nota1 + nota2) / 2

if media < 7 :
    print("Reprovado!")
elif media == 10:
    print("Aprovado com distinção!!")
else:
    print("Aprovado!")

