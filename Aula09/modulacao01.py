# Nesta aula iremos aprender sobre modulação que em outras linguagens pode ser conhecida como função, método e etc.
# Modulação é uma forma de organizar o código, dividindo em partes menores, que podem ser chamadas de funções ou métodos

# Exemplo de função:
# def nome_da_funcao(parametros):
#   codigo

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b) :
    if b == 0:
        return "Não é possível dividir por zero"
    else:
        return a / b

# Chamada da função ou método:   
print(soma(1, 2))

numero = 20
numero2 = 40

print("A multiplicação é igual a: ", multiplicacao(numero, numero2))

print("A divisão é igual a: ", divisao(numero, numero2))