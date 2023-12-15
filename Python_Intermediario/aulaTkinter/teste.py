import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")

# Criar botões e entradas de texto
botao_soma= tk.Button(janela, text="+")
botao_subtracao = tk.Button(janela, text="-")
# .. criar entradas

# posicionar os widgets na janela
botao_soma.grid(row=0, column=0)
botao_subtracao.grid(row=0, column=1)



# motrar janela