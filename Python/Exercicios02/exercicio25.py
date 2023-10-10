# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a 
# média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

pessoas = int(input("Informe a quantidade de pessoas: "))

somaIdade = 0

for i in range(0,pessoas):
    idade = int(input(f"Informe a idade da {i+1}° pessoa: "))
    somaIdade = somaIdade + idade

media = somaIdade / pessoas

# print(media)

if media <= 25:
    print("Esse conjunto de pessoas jovens!")
elif media > 25 and  media <= 60:
    print("Esse conjunto de pessoas adultas!")
else:
    print("Esse conjunto de pessoas idosas!")

