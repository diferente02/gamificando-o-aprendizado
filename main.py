from tkinter import * # Importa tudo do tkinter, incluindo widgets básicos
from tkinter import ttk # Importa o submódulo ttk com widgets mais modernos e estilizados.

#2.0.0
porcentagemBarra = 0
varBarra = 0

#2.1.0
def Tela_principal(Variavel_app):
    global varBarra

    #2.1.1
    texto_2 = Label(text="Tela", font="Arial 24")
    #retirado as aspas do numeros
    texto_2.place(x=100, y=100)
    
    #2.1.2
    varBarra = DoubleVar()
    varBarra.set(0) # o quanto a barra estará preenchida 
    barra_de_progresso = ttk.Progressbar(Variavel_app,variable=varBarra,maximum=100)
    barra_de_progresso.place(x=40, y=10)

    #2.1.3
    var_num_nivel = StringVar()
    var_num_nivel.set("0") 
    Numero_do_nivel = Label(textvariable=var_num_nivel)
    Numero_do_nivel.place(x=20, y=5)

    #2.1.4
    botao = ttk.Button(Variavel_app,width=20, text="botao",command= lambda:click_aumento_da_barra_de_progressao(texto_2, var_num_nivel))
    botao.place(x=15,y=60)

    #2.1.5
    ## =============================== Variable second =============================
    sec = StringVar()
    Label(Variavel_app, textvariable=sec, width=2, font="Arial 14").place(x='155', y='180')
    sec.set(0)

    # ===================== just two points (:) ===================================
    Label(Variavel_app, text=':', font='Arial 16').place(x='145', y='180')

    # ======================== Variable minutes ====================================
    min = StringVar()
    Label(Variavel_app, textvariable=min, width=2, font="Arial 14").place(x='120', y='180')
    min.set(0)



#2.2.0
def click_aumento_da_barra_de_progressao(texto_2, var_num_nivel):
        #2.2.1
        global porcentagemBarra
        porcentagemBarra = porcentagemBarra + 10
        varBarra.set(porcentagemBarra)

        #2.2.2
        if porcentagemBarra == 100:
            nivel_velho = int(var_num_nivel.get()) 
            novo_nivel = nivel_velho + 1
            var_num_nivel.set(novo_nivel)

            texto_2['text']="concluida"
            porcentagemBarra = 0