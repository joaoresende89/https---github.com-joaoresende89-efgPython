# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

telefone = input("Telefonou para a vítima? ")
local = input("Esteve no local do crime? ")
mora = input("Mora perto da vítima? ")
deve = input("Devia algo para a vítima? ")
trabalho = input("Já trabalhou com a vítima? ")

culpabilidade = 0

if telefone.lower() == 'sim':
    culpabilidade = culpabilidade + 1
if local.lower() == 'sim':
    culpabilidade = culpabilidade + 1
if mora.lower() == 'sim':
    culpabilidade = culpabilidade + 1
if deve.lower() == 'sim':
    culpabilidade = culpabilidade + 1
if trabalho.lower() == 'sim':
    culpabilidade = culpabilidade + 1

if culpabilidade < 2:
    print("Inocente!")
if culpabilidade == 2:
    print("Suspeita!")
if culpabilidade > 2 and culpabilidade <= 4:
    print("Cúmplice!")
if culpabilidade == 5:
    print("Culpado!!")

