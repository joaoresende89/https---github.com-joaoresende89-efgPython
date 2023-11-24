# Cadastro de alunos e notas. O programa derevá permitir inserir até 30 aluno, com os seguintes campo: nome, telefone, email e endereço completo
# além deverá ser possível adicionar a nota do aluno e uma média final deverá ser calculada. Serão 4 notas, que representam cada um dos bimestres.
# Adicionalmente poderá ser as notas que poderão representar cada uma das disciplinas.

# aluno = []

# chave = 0

# while chave < 30:
#     aluno.append(cadastroAluno())
#     opcao = int(input("Para cadastrar mais alunos digite 1 ou digite 0 para sair: "))
#     if opcao == 0:
#         chave = 30
#     chave += 1

# print(aluno)

# print(calculaMedia(aluno[0]))


# função para cadastrar aluno
def cadastroAluno():
    Aluno = dict()
    Aluno['Nome'] = input("Nome do aluno: ")
    Aluno['Telefone'] = input("Telefone: ")
    Aluno['Email'] = input("Email: ")
    Aluno['Endereco'] = input("Endereço: ")
    Aluno['Notas'] = [float(input("Informe a nota1: ")), float(input("Informe a nota2: ")), float(input("Informe a nota3: ")), float(input("Informe a nota4: "))]
    return Aluno

# listar alunos
def listarAlunos(a):
    i = len(a)
    for j in range(0,i):
        print(a[j])
    return 0

# função para cacular a média das notas
def calculaMedia(teste):
    teste['Media'] = sum(teste['Notas']) / 4
    print(f"Media das notas do aluno {teste['Nome']} é {teste['Media']}")
    return teste

# pesquisar aluno
def pesquisaAluno(aluno):
    nome = input("Informe o nome do aluno a ser buscado: ")
    for i in range(len(aluno)):
        if aluno[i]['Nome'] == nome:
            return aluno[i]
        else:
            print("Aluno não econtrado!")
            return 0

aluno = []

def menu():
    opcao = 1
    while opcao != 0:
        print('''
        -------------------ALUNOS----------------------
        |       Escolha uma opção abaixo:              |
        |   1 - Cadastrar aluno                        |
        |   2 - Calcular e mostrar média do aluno      |      
        |   3 - Listar alunos                          |
        |   4 - Pesquisar aluno                        |
        |   0 - Sair                                   |
        |______________________________________________|
        ''')
        
        opcao = int(input("Digite uma das opções ou 0 para sair: "))

        if opcao == 1:
            if len(aluno) == 30:
                print("Não é possível cadastrar mais alunos!")
            else:
                aluno.append(cadastroAluno())
        elif opcao == 2:
            calculaMedia(aluno)
        elif opcao == 3:
            listarAlunos(aluno)
        elif opcao == 4:
            pesquisaAluno(aluno)
        else:
            print("Opção inválida!")

menu()
