from tkinter import * # Importa tudo do tkinter, incluindo widgets básicos
from tkinter import ttk # Importa o submódulo ttk com widgets mais modernos e estilizados.


def click_aumento_da_barra_de_progressao():
    global porcentagemBarra  
    porcentagemBarra= porcentagemBarra + 10
    varBarra.set(porcentagemBarra)
    if porcentagemBarra == 100:
        label['text']="concluida"
        porcentagemBarra = 0


root = Tk()
varBarra = DoubleVar()
varBarra.set(0) # o quanto a barra estará preenchida 
porcentagemBarra = 0

pb = ttk.Progressbar(root,
    variable=varBarra,
    maximum=100)
pb.place(x=20, y=30)

label = Label(root, text="hello world")
label.place(x=20, y=7)

botao = ttk.Button(root,width=20, text="botao", command=click_aumento_da_barra_de_progressao)
botao.place(x=15,y=60)




root.mainloop()

