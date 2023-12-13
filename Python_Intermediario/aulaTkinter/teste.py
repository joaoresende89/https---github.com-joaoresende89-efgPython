from tkinter import ttk
import tkinter


class jogo:
    def __init__(self,root):
        self.Formulario()

    # Função que é chamada no botão salvar e quando clica no X do programa
    def SalvarInformacoes(self, finalizarPrograma = True):
        # Cria um arquivo
        with open("testeFile.txt", 'w') as f:
            # Escreve as informações que foram preenchidas no front, pode ser trocado por um banco de dados
            f.write(self.Nome.get() + '\n')
            f.write(self.Cidade.get() + '\n')
        if (finalizarPrograma):
            root.destroy()

    def CarregarInformacoes(self):
        try:
            # Função que é chamda quando termina de desenhar o formulário, inserindo a informação que está preenchida no arquivo
            with open("testeFile.txt", 'r') as f:
                nome = f.readline().replace("\n", "")
                cidade = f.readline().replace("\n", "")
                self.Nome.insert(0, nome)
                self.Cidade.insert(0, cidade)
            #caso o arquivo não exista vai cair no exception e simplesmente n vai carregar nada
        except Exception:
            pass

    def Formulario (self):
        # Protocolo que detecta o click no X do Frame
        root.protocol("WM_DELETE_WINDOW", self.SalvarInformacoes)
        self.formulario = ttk.Frame(root)
        self.formulario.pack()
        v= tkinter.IntVar()
        ttk.Checkbutton(self.formulario,text = "check1",variable = v).pack()

        lbl_entry = ttk.Label(self.formulario, text = "nome:")
        lbl_entry.pack()
        self.Nome = ttk.Entry(self.formulario)
        self.Nome.pack()
        lbl_entry2 = ttk.Label(self.formulario, text = "cidade:")
        lbl_entry2.pack()
        self.Cidade = ttk.Entry(self.formulario)
        self.Cidade.pack()
        
        bt= ttk.Button(self.formulario,text = "salvar", command = lambda : self.SalvarInformacoes(finalizarPrograma = False))
        bt.pack()
        self.CarregarInformacoes()
    
root = tkinter.Tk()
jogo(root)
root.mainloop()