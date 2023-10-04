# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# import getpass

nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")

while senha.lower() == nome.lower():
    print("A senha não pode ser igual ao nome!")
    senha = input("Informe outra senha: ")

print("Dados ok!") 