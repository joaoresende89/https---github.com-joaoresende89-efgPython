# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print("Informe os lados do triangulo:")
lado1 = input("Informe o primeiro lado: ")
lado2 = input("Informe o segundo lado: ")
lado3 = input("Informe o terceiro lado: ")

if lado1 == lado2 and lado1 == lado3:
    print("Este triangulo é Equilátero!")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Este triangulo é Isósceles!")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Este triangulo é Escaleno!")

