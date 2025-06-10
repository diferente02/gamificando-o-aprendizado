from tkinter import * # Importa tudo do tkinter, incluindo widgets básicos
from tkinter import ttk # Importa o submódulo ttk com widgets mais modernos e estilizados.
from time import sleep
from pyautogui import confirm, alert
import pyttsx3

engine = pyttsx3.init()



#2.0.0
# ----------------------------- countdowntimer -------------------------------
def countdowntimer(Variavel_app,sec,min,titulo, tempo_em_segundos=None, callback_final=None):
    #2.0.1
    titulo.get()
    titulo.set("FORÇA,FOCO E FÉ")
    if tempo_em_segundos is None:
        tempo_em_segundos = 10  # tempo padrão: 10 segundos

    #2.0.2
    if tempo_em_segundos >= 0:
        minute, second = (tempo_em_segundos // 60, tempo_em_segundos % 60)
        sec.set(second)
        min.set(minute)
        Variavel_app.after(1000, lambda: countdowntimer(Variavel_app, sec, min,titulo, tempo_em_segundos - 1, callback_final))
    else:
        sec.set('00')
        min.set('00')
        if callback_final:
            callback_final()
            #engine.say(f'Tempo finalizdo')  # aviso sonoro que acabou
            #engine.runAndWait()
            alert(title='Foco',
                text='tempo de foco terminado, descanse um pouco')  # janela de alerta, avisado que o tmepo de descanso terminou, só avisa mesmo
            descanso(Variavel_app,sec,min,titulo, tempo_em_segundos=None)

def descanso(Variavel_app,sec,min,titulo, tempo_em_segundos=None):  # função descanso
        titulo.get()
        titulo.set("DESCANSAR NÉ, NINQUÉM É DE FERRO")
        if tempo_em_segundos is None:
            tempo_em_segundos = 5
            
        if tempo_em_segundos >= 0:
            # converte o tempo em segundos para minutos 
            minute, second = (tempo_em_segundos // 60, tempo_em_segundos % 60)
            sec.set(second)
            min.set(minute)
            # Update the time
            Variavel_app.after(1000, lambda: descanso(Variavel_app,sec,min,titulo,tempo_em_segundos-1))  # depois de 1 segundo (1000 ms) chama a função descanso denovo

        else:  # quando a contagem terminar fica com "00" ao invés de "0"
            sec.set('00')
            min.set('00')
            # engine.say(f'O tempo de descanso acabou')  # aviso falado que o tempo de descanso acabou
            # engine.runAndWait()
            alert(title='Descanso',
              text='tempo de descanso terminado')  # janela de alerta, avisado que o tmepo de descanso terminou, só avisa mesmo
            
        

#2.1.0
def Tela_principal(Variavel_app):
    global varBarra

    #2.1.1
    titulo = StringVar()
    titulo.set("Foco")
    Label(textvariable=titulo, font="Arial 12").place(x=100, y=100)
    
    #2.1.2
    progresso_concluido = IntVar()
    progresso_concluido.set(0)
    Label(textvariable=progresso_concluido).place(x=290, y=10)

    Label(text="/").place(x=310, y=10)
    valor_maximo = IntVar()
    valor_maximo.set(20)
    Label(textvariable=valor_maximo).place(x=320, y=10)

    #2.1.3
    varBarra = IntVar()
    varBarra.set(0) # o quanto a barra estará preenchida 
    barra_de_progresso = ttk.Progressbar(Variavel_app,length=250, variable=varBarra,maximum=valor_maximo.get())
    barra_de_progresso.place(x=30, y=10)

    #2.1.4
    var_num_nivel = IntVar()
    var_num_nivel.set(0) 
    Label(textvariable=var_num_nivel).place(x=10, y=5)

    #2.1.5
    botao = ttk.Button(Variavel_app,width=20, text="botao",command= lambda:click_aumento_da_barra_de_progressao(titulo, var_num_nivel,valor_maximo, progresso_concluido))
    #botao.place(x=15,y=60)

    #2.1.6
    ## =============================== Variable second =============================
    sec = StringVar()
    Label(Variavel_app, textvariable=sec, width=2, font="Arial 32").place(x='165', y='180')
    sec.set(0)

    # ===================== just two points (:) ===================================
    Label(Variavel_app, text=':', font='Arial 56').place(x='145', y='160')

    # ======================== Variable minutes ====================================
    min = StringVar()
    Label(Variavel_app, textvariable=min, width=2, font="Arial 32").place(x='100', y='180')
    min.set(0)

    #2.1.7
    botao_iniciar = ttk.Button(Variavel_app, width=20, text="iniciar contagem", command= lambda: countdowntimer(
         Variavel_app,sec,min,titulo,
        callback_final=lambda: click_aumento_da_barra_de_progressao(titulo,var_num_nivel, valor_maximo, progresso_concluido)
    ) )
    botao_iniciar.place(x="110", y="300")


#2.2.0
def click_aumento_da_barra_de_progressao(titulo, var_num_nivel, valor_maximo, progresso_concluido):
        #2.2.1
        progresso_novo = progresso_concluido.get() + 10
        progresso_concluido.set(progresso_novo)
        varBarra.set(progresso_novo)

        #2.2.2
        if progresso_novo == valor_maximo.get():

            nivel_velho = var_num_nivel.get()
            novo_nivel = nivel_velho + 1
            var_num_nivel.set(novo_nivel)

            novo_valor_max = valor_maximo.get() + 10
            valor_maximo.set(novo_valor_max)

            varBarra.set(0)

            titulo.get()
            titulo.set("Parabens você subiu de nível")
    
            progresso_concluido.set(0)