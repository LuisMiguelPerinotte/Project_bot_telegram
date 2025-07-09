import tkinter as tk

def inicio_interface():
    janela = tk.Tk()
    janela.title("LM BOT")
    janela.geometry("600x400")
    
    label = tk.Label(janela, text="BOT EM EXECUÇÃO..." )
    label.pack(pady=20)

    botão_sair = tk.Button(janela, text="Parar Bot", command=janela.destroy)
    botão_sair.pack(pady=10)
    
    janela.mainloop()