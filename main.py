from tkinter import * # Importa tudo do tkinter, incluindo widgets básicos
from tkinter import ttk # Importa o submódulo ttk com widgets mais modernos e estilizados.

#2.0.0
porcentagemBarra = 0
varBarra = 0

#2.1.0
def Tela_principal(Variavel_app):
    global varBarra

    #2.1.1
    texto_2 = Label(text="Funcionou", font="Arial 24")
    texto_2.place(x="100", y="100")
    
    #2.1.2
    varBarra = DoubleVar()
    varBarra.set(0) # o quanto a barra estará preenchida 
    pb = ttk.Progressbar(Variavel_app,variable=varBarra,maximum=100)
    pb.place(x=30, y=5)

    #2.1.3
    Numero_do_nivel = Label(text=0)
    Numero_do_nivel(x=20, y=5)

    #2.1.4
    botao = ttk.Button(Variavel_app,width=20, text="botao",command= lambda:click_aumento_da_barra_de_progressao(texto_2))
    botao.place(x=15,y=60)


#2.2.0
def click_aumento_da_barra_de_progressao(texto_2):
        #2.2.1
        global porcentagemBarra
        porcentagemBarra = porcentagemBarra + 10
        varBarra.set(porcentagemBarra)
        if porcentagemBarra == 100:
            texto_2['text']="concluida"
            porcentagemBarra = 0