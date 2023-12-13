# TKINTER

from tkinter import *
import tkinter.messagebox

janela = Tk()
menubar = Menu(janela)
janela.config(menu=menubar)
janela.title("CADASTRO DE ALUNOS")
janela.geometry("400x400")

# vetor de alunos

alunos = []

# criando menu
cadastroMenu = Menu(menubar)
menubar.add_cascade(label="Cadastro", menu=cadastroMenu)
menubar.add_command(label="Sobre")

def limpa_tela():
    cadastroAluno.destroy()
    

# função da tela de cadastro
def cadastroAluno():
    #criando outra janela para cadastro
    janela_cadastro = Tk()
    janela_cadastro.title("Cadastro de Aluno")
    janela_cadastro.geometry("400x400")
    # gravar os dados no dicionario aluno
    def cadastro():
        Aluno = dict()
        Aluno['nome'] = entry_nome.get()
        Aluno['telefone'] = entry_telefone.get()
        Aluno['email'] = entry_email.get()
        Aluno['endereço'] = entry_endereco.get()
        Aluno['notas'] = {
            'nota1': float(entry_nota1.get()),
            'nota2': float(entry_nota2.get()),
            'nota3': float(entry_nota3.get()),
            'nota4': float(entry_nota4.get())
        }
        alunos.append(Aluno)
        tkinter.messagebox.showinfo("Cadastro de Aluno", "Aluno cadastrado com sucesso!")
        MsgBox = tkinter.messagebox.askyesno(message="Deseja casdastrar mais um aluno?")
        if MsgBox == True:
            # limpar a tela
            entry_nome.delete(0, END)
            entry_telefone.delete(0, END)
            entry_email.delete(0, END)
            entry_endereco.delete(0, END)
            entry_nota1.delete(0, END)
            entry_nota2.delete(0, END)
            entry_nota3.delete(0, END)
            entry_nota4.delete(0, END)
        else:
            janela_cadastro.destroy()            
    

    # Rótulos Entradas
    label_nome = Label(janela_cadastro, text='Nome')
    label_nome.grid(row=0,column=0, padx=10, pady=10)

    label_telefone = Label(janela_cadastro, text='Telefone')
    label_telefone.grid(row=1, column=0, padx=10, pady=10)

    label_email = Label(janela_cadastro, text='E-mail')
    label_email.grid(row=2, column=0 , padx=10, pady=10)

    label_endereco = Label(janela_cadastro, text='Endereço')
    label_endereco.grid(row=3, column=0, padx=10, pady=10)

    label_nota1 = Label(janela_cadastro, text='Nota1')
    label_nota1.grid(row=4, column=0, padx=10, pady=10)

    label_nota2 = Label(janela_cadastro, text='Nota2')
    label_nota2.grid(row=5, column=0, padx=10, pady=10)

    label_nota3 = Label(janela_cadastro, text='Nota3')
    label_nota3.grid(row=6, column=0, padx=10, pady=10)

    label_nota4 = Label(janela_cadastro, text='Nota4')
    label_nota4.grid(row=7, column=0, padx=10, pady=10)

    # Caixas entradas
    entry_nome = Entry(janela_cadastro, width =45)
    entry_nome.grid(row=0,column=1, padx=10, pady=10)

    entry_telefone = Entry(janela_cadastro, width =45)
    entry_telefone.grid(row=1,column=1, padx=10, pady=10)

    entry_email = Entry(janela_cadastro, width =45)
    entry_email.grid(row=2,column=1, padx=10, pady=10)

    entry_endereco = Entry(janela_cadastro, width =45)
    entry_endereco.grid(row=3,column=1, padx=10, pady=10)

    entry_nota1 = Entry(janela_cadastro, width =45)
    entry_nota1.grid(row=4,column=1, padx=10, pady=10)

    entry_nota2 = Entry(janela_cadastro, width =45)
    entry_nota2.grid(row=5,column=1, padx=10, pady=10)

    entry_nota3 = Entry(janela_cadastro, width =45)
    entry_nota3.grid(row=6,column=1, padx=10, pady=10)

    entry_nota4 = Entry(janela_cadastro, width =45)
    entry_nota4.grid(row=7,column=1, padx=10, pady=10)

    # botao cadastrar e chamar a função para gravar 

    botaoCad = Button(janela_cadastro, text="Cadastrar", command=cadastro)
    botaoCad.grid(row=8)
    boatao_cancel = Button(janela_cadastro, text="Cancelar", command=janela_cadastro.destroy)
    boatao_cancel.grid(row=8, column=1)

    janela_cadastro.mainloop()

# função para listar os alunos
def listarAlunos():
    janela_listar = Tk()
    janela_listar.title("Lista de Alunos")

    for i in range(len(alunos)):
        aux = {}
        aux = alunos[i]
        print(aux)
        # for j in range(len(aux[0])):
        #     lista = Entry(janela_listar, width=12)
        #     lista.grid(row=i, column=j)
        #     lista.insert(END, aux[i][j])    

    janela_listar.mainloop()
    

# criando sub menus
cadastroMenu.add_command(label="Cadastrar aluno", command=cadastroAluno)
cadastroMenu.add_command(label="Calcular e mostrar média do aluno ")
cadastroMenu.add_command(label="Listar alunos", command=listarAlunos)
cadastroMenu.add_command(label="Pesquisar aluno")
cadastroMenu.add_separator()
cadastroMenu.add_command(label="Sair", command=janela.destroy)

janela.mainloop()


