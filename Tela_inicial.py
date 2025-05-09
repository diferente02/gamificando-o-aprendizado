from tkinter import * # Importa tudo do tkinter, incluindo widgets básicos
from tkinter import ttk # Importa o submódulo ttk com widgets mais modernos e estilizados.
import main

#1.0.3
def Fechando_tela_inicial():
    texto_1.place_forget()
    botao_iniciar.place_forget()
    main.Tela_principal(app)

#1.0.0
app = Tk()
app.geometry("350x500")

#1.0.1
texto_1 = Label(text="Texto 1", font="Arial 24")
texto_1.place(x="125", y="100")

#1.0.2
botao_iniciar = ttk.Button(app,text="Iniciar", width=25, command=Fechando_tela_inicial)
botao_iniciar.place(x="110", y="300")


app.mainloop()