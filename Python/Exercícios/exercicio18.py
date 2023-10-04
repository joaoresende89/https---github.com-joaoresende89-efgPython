# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Informe a data (DD/MM/AAAA): ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

dia = int(dia)
mes = int(mes)
ano = int(ano)

if (ano % 100 != 0) and ((ano % 4 == 0) or (ano % 400 == 0)):
    if dia > 0 and mes > 0 and ano > 0:
        if mes > 12:
            print("Data inválida!")
            exit()
        if mes == 2 and dia > 29:
            print("Data inválida")
            exit()
        if mes in (1, 3, 5, 7, 8, 10, 12) and dia > 31:
            print("Data inválida")
            exit()
        if mes in (4, 6, 9, 11) and dia > 30:
            print("Data inválida")
            exit()
        print("Data válida: ",dia,"/",mes,"/",ano)
    else:
        print("Data inválida!")
        exit()
else:
    if dia > 0 and mes > 0 and ano > 0:
        if mes > 12:
            print("Data inválida!")
            exit()
        if mes == 2 and dia > 28:
            print("Data inválida")
            exit()
        if mes in (1, 3, 5, 7, 8, 10, 12) and dia > 31:
            print("Data inválida")
            exit()
        if mes in (4, 6, 9, 11) and dia > 30:
            print("Data inválida")
            exit()
        print("Data válida: ",dia,"/",mes,"/",ano)
    else:
        print("Data inválida!")
        exit()



