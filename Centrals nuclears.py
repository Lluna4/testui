import tkinter 
import time
from tkinter import filedialog, Text
import os
import sys






explicacion_partes1 = "-Vas del reactor: És un recipient on es produeix la fissió hi estan el combustible (urani o plutoni) i l'irradiador de neutrons, per trencar els nuclis"
explicacion_partes11 = "del combustible"
explicacion_partes2 = "-Moderador: Redueix la velocitat del neutrons, per assegurar la fissió i fer-la mes llarga, els moderadors mes utilitzats son l'aigua, l'aigua pesant"
explicacion_partes3 = "(format per atoms d'hidrogen amb 2 neutrons, mes conegut com deuteri) i el grafit"
explicacion_tipos_PWR1 = "Es el mes usat a nivell mundial, el refrigrant es impulsat per tot el vas i er l'intercambiador o generador de vapor, el pressionador fa que que l'aigua"
explicacion_tipos_PWR12 = "del refrigerador no entri en ebullició.El generador de vapor transfereix la calor del primer circuit al segon on l'aigua s'evapora i s'introdueix al"
explicacion_tipos_PWR13 = "reescalfador per eliminar l'humitat i així es converteix en vapor sec, i entra a la turbina on gracies a la pressió del gas la fa girar i produeix energia."
explicacion_tipos_PWR2 = "Despres de passar per la turbina, es va al condensador on torna a estat liquid i repeteix el procés."
explicacion_tipos_BWR1 = "Es un sistema on l’aigua actua com a moderador(sustancia utilitzada per fer mes lentes les reaccions) i com a refrigerant al mateix temps, l’aigua"
explicacion_tipos_BWR2 = "que entra en ebullició es pasa a un assecador per a fer un vapor sec i despres a la turbina. El circuit te que ser tancat perque l’aigua ha estat "
explicacion_tipos_BWR3 = "en contacte amb el combustible"
explcacion_tipos_NR1 = "Son centrals sense moderador, aixi que la reacció es molt mes rapida, per tant es necessita un gran volum de combustble, per evitar sobrecalentaments"
explcacion_tipos_NR2 = "s’utilitzen dos circuits de refrigeració amb sodi liquid, s’utilitzen com combustibles l’urani 235 i el plutoni 239 recoberts per urani 238 que al absorbir"
explcacion_tipos_NR3 = " neutrons es converteix en plutoni 239 i aixo fa que es produeixi mes combustible del que es gasta, el fucionament del circuit de vapor es un circuit"
explcacion_tipos_NR4 = "que entra en ebullició i aquest vapor es seca i entra al transformador, es condensa i torna al circuit"
explcacion_equipamiento_EC1 = "En el seu interior té el reactor i el circuit primari, està fet per formigó especial folrat d’acer per evitar qualsevol emissió inclus en un accident"
explcacion_equipamiento_EC2 = ", es tan estable que resisteix terratremols."
explcacion_equipamiento_ET1 = "A dintre estan la turbina i l’alternador (encargats de transformar l’ energia cinetica del vapor a electrica), tambe la part que condensa el vapor, els"
explcacion_equipamiento_ET2 = "prescalfadors i els rescalfadors. En les centrals BWR esta protegit de les emissions de l’aigua radioactiva"
explcacion_equipamiento_ECom1 = "Emmagatzema el combustible del reactor i el combustible ja utilitzat en espera per el seu reprocessament. El combustible que no ha sigut utilitzat"
explcacion_equipamiento_ECom2 = "s'emmagatzema en piscines de formigó folrat amb acer (com la capa exterior de l’edifici de contenció) i que ja ha estat utilitzat s’emmagatzema"
explcacion_equipamiento_ECom3 = "en piscines d’aigua. Aquest edifici esta connectat amb el reactor per fer la recarrega de combustible lo mes segura possible i sense emissions."
explcacion_equipamiento_ECon1 = "A dintre hi esta la sala de control, lloc on es monitoritza tota la central i on es donen ordres en base a les dades que s’han rebut."
explcacion_equipamiento_ECon2 = "Aquest proces esta automatizat per l’ordinador central."
explcacion_equipamiento_EAux1 = "A dintre hi han sistemes de seguretat i sistemes auxiliars per si els principals fallen, també hi estan els sistemes de tractament de residus d’activitat baixa,"
explcacion_equipamiento_EAux2 = "l’equip de filtratge i l’aire condicionat de l’edifici de contenció i el seu propi."
explicacion_funcionamiento1 = "L'energia en forma de vapor a altes pressions es transportat del reactor a la turbina on produeix energia elèctrica per després anar al l’alternador on es lliura a la"
explicacion_funcionamiento2 = "xarxa, el vapor que ha passat per la turbina es condensa per després tornar-se a vaporitzar, i així es tanca el circuit, en canvi el circuit de refrigeració és obert,"
explicacion_funcionamiento3 = "per tant, l’aigua que s’utilitza prové d’un riu que al terminar al seu recorregut torna al riu, si el riu és escàs, es refreda abans de tornar al riu."
root = tkinter.Tk()
root.title("Centrals nuclears")


def Partes():
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()   
    for widget in frame2.winfo_children():
        widget.destroy()
    titulo = tkinter.Label(frame2, text="Parts", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    texto_en_pantala = tkinter.Label(frame2, text=explicacion_partes1, bg="black", fg="green")
    texto_en_pantala2 = tkinter.Label(frame2, text=explicacion_partes11, bg="black", fg="green")
    texto_en_pantala3 = tkinter.Label(frame2, text=explicacion_partes2, bg="black", fg="green")
    texto_en_pantala4 = tkinter.Label(frame2, text=explicacion_partes3, bg="black", fg="green")
    
    print("pulsado")
    titulo.pack(side="top")
    texto_en_pantala.pack(side="top")
    texto_en_pantala2.pack(side="top")
    texto_en_pantala3.pack(side="top")
    texto_en_pantala4.pack(side="top")
    partes.pack(side="top")
    tipos.pack(side="top")




def Tipos():
    volver_boton_PWR.pack_forget()
    partes.pack_forget()
    tipos.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    titulo = tkinter.Label(frame2, text="Sobre que part vols saber?", bg="black", fg="green")
    titulo.config(font=("arial", 30)) 
    titulo.pack(side="top")
    
    PWR_boton.pack(side="top")
    
    BWR_boton.pack(side="top")
    
    NR_boton.pack(side="top")
    volver_boton_Tipos.pack(anchor=tkinter.E)

     
    titulo.pack(side="top")
    

def Equipamiento():
    volver_boton_equipamiento.pack_forget()
    partes.pack_forget()
    tipos.pack_forget() 
    equipamiento.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    
    
    titulo1 = tkinter.Label(frame2, text="Sobre que part del", bg="black", fg="green")
    titulo2 = tkinter.Label(frame2, text="equipament vols saber?", bg="black", fg="green")
    titulo1.config(font=("arial", 40))
    titulo1.pack(side="top")
    titulo2.config(font=("arial", 40))
    titulo2.pack(side="top")
    volver_boton_equipamiento_inicio.pack(anchor=tkinter.E)
    EC.pack(side="top")
    ET.pack(side="top")
    ECom.pack(side="top")
    ECon.pack(side="top")
    EAux.pack(side="top")



def EC():
    volver_boton_equipamiento_inicio.pack_forget()
    EC.pack_forget()
    ECom.pack_forget()
    ECon.pack_forget()
    EAux.pack_forget()
    ET.pack_forget()
    
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    titulo = tkinter.Label(frame2, text="Edifici de contenció", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()

    texto_EC1 = tkinter.Label(frame2, text=explcacion_equipamiento_EC1, bg="black", fg="green")
    texto_EC1.pack(side="top")
    texto_EC2 = tkinter.Label(frame2, text=explcacion_equipamiento_EC2, bg="black", fg="green")
    texto_EC2.pack(side="top")
    
    volver_boton_equipamiento.pack(side="top")



def ET():
    volver_boton_equipamiento_inicio.pack_forget()
    EC.pack_forget()
    ECom.pack_forget()
    ECon.pack_forget()
    EAux.pack_forget()
    ET.pack_forget()
    
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()

    titulo = tkinter.Label(frame2, text="Edifici de turbines", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()

    texto_ET1 = tkinter.Label(frame2, text=explcacion_equipamiento_ET1, bg="black", fg="green")
    texto_ET1.pack(side="top")
    texto_ET2 = tkinter.Label(frame2, text=explcacion_equipamiento_ET2, bg="black", fg="green")
    texto_ET2.pack(side="top")

    volver_boton_equipamiento.pack(side="top")

    

def ECOM():
    volver_boton_equipamiento_inicio.pack_forget()
    EC.pack_forget()
    ECom.pack_forget()
    ECon.pack_forget()
    EAux.pack_forget()
    ET.pack_forget()
    
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    titulo = tkinter.Label(frame2, text="Edifici de combustible", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()

    texto_ECom1 =tkinter.Label(frame2, text=explcacion_equipamiento_ECom1, bg="black", fg="green")
    texto_ECom2 =tkinter.Label(frame2, text=explcacion_equipamiento_ECom2, bg="black", fg="green")
    texto_ECom3 =tkinter.Label(frame2, text=explcacion_equipamiento_ECom3, bg="black", fg="green")
    
    texto_ECom1.pack(side="top")
    texto_ECom2.pack(side="top")
    texto_ECom3.pack(side="top")
    volver_boton_equipamiento.pack(side="top")


def ECOn():
    volver_boton_equipamiento_inicio.pack_forget()
    EC.pack_forget()
    ECom.pack_forget()
    ECon.pack_forget()
    EAux.pack_forget()
    ET.pack_forget()
    
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    titulo = tkinter.Label(frame2, text="Edifici de control", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()
    
    texto_Econ1 = tkinter.Label(frame2, text=explcacion_equipamiento_ECon1, bg="black", fg="green")
    texto_Econ2 = tkinter.Label(frame2, text=explcacion_equipamiento_ECon2, bg="black", fg="green")
   
    texto_Econ1.pack(side="top")
    texto_Econ2.pack(side="top")
    volver_boton_equipamiento.pack(side="top")


def EAUX():
    volver_boton_equipamiento_inicio.pack_forget()
    EC.pack_forget()
    ECom.pack_forget()
    ECon.pack_forget()
    EAux.pack_forget()
    ET.pack_forget()
    
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    titulo = tkinter.Label(frame2, text="Edifici auxiliar", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()

    texto_EAux1 = tkinter.Label(frame2, text=explcacion_equipamiento_EAux1, bg="black", fg="green")
    texto_EAux2 = tkinter.Label(frame2, text=explcacion_equipamiento_EAux2, bg="black", fg="green")
    texto_EAux1.pack(side="top")
    texto_EAux2.pack(side="top")
    volver_boton_equipamiento.pack(side="top")




def Funcionamiento():
    volver_boton_equipamiento.pack_forget()
    partes.pack_forget()
    tipos.pack_forget() 
    equipamiento.pack_forget()
    Funcionamiento_boton.pack_forget()
    for widget in frame.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    titulo = tkinter.Label(frame2, text="Funcionament", bg="black", fg="green")
    titulo.config(font=("arial", 50))
    titulo.pack()

    texto_funcionamiento1 = tkinter.Label(frame2, text=explicacion_funcionamiento1, bg="black", fg="green")
    texto_funcionamiento2 = tkinter.Label(frame2, text=explicacion_funcionamiento2, bg="black", fg="green")
    texto_funcionamiento3 = tkinter.Label(frame2, text=explicacion_funcionamiento3, bg="black", fg="green")
    texto_funcionamiento1.pack(side="top")
    texto_funcionamiento2.pack(side="top")
    texto_funcionamiento3.pack(side="top")
    volver_boton_funcionamiento_inicio.pack(side="top")



    
    


def PWR():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
    NR_boton.pack_forget()
    for widget in frame2.winfo_children():
        widget.destroy()
    titulo1 = tkinter.Label(frame2, text="PWR", bg="black", fg="green")
    titulo1.config(font=("arial", 50))
    texto_en_pantala21 = tkinter.Label(frame2, text=explicacion_tipos_PWR1, bg="black", fg="green")
    texto_en_pantala22 = tkinter.Label(frame2, text=explicacion_tipos_PWR12, bg="black", fg="green")
    texto_en_pantala23 = tkinter.Label(frame2, text=explicacion_tipos_PWR13, bg="black", fg="green")
    texto_en_pantala24 = tkinter.Label(frame2, text=explicacion_tipos_PWR2, bg="black", fg="green")

    print("pulsado")
    titulo1.pack(side="top")
    texto_en_pantala21.pack(side="top")
    texto_en_pantala22.pack(side="top")
    texto_en_pantala23.pack(side="top")
    texto_en_pantala24.pack(side="top")

    volver_boton_PWR.pack(side="top")
    



    intro3 = tkinter.Label(frame2, text="Vols saber mes? Pulsa un dels botons a baix per saber mes sobre les centrals nuclears", bg="black", fg="green")
    intro3.pack()
  
def BWR():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
    NR_boton.pack_forget()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    tituloBWR = tkinter.Label(frame2, text="BWR", bg="black", fg="green")
    tituloBWR.config(font=("arial", 50))
    tituloBWR.pack(side="top")

    texto_BWR1 = tkinter.Label(frame2, text=explicacion_tipos_BWR1, bg="black", fg="green")
    texto_BWR2 = tkinter.Label(frame2, text=explicacion_tipos_BWR2, bg="black", fg="green")
    texto_BWR3 = tkinter.Label(frame2, text=explicacion_tipos_BWR3, bg="black", fg="green")

    texto_BWR1.pack(side="top")
    texto_BWR2.pack(side="top")
    texto_BWR3.pack(side="top")
    volver_boton_PWR.pack(side="top")
    

def NR():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
    NR_boton.pack_forget()
    for widget in frame2.winfo_children():
        widget.destroy()
    
    tituloNR = tkinter.Label(frame2, text="Neutrons Rapids", bg="black", fg="green")
    tituloNR.config(font=("arial", 40))
    tituloNR.pack(side="top")

    texto_NR1 = tkinter.Label(frame2, text=explcacion_tipos_NR1, bg="black", fg="green")
    texto_NR2 = tkinter.Label(frame2, text=explcacion_tipos_NR2, bg="black", fg="green")
    texto_NR3 = tkinter.Label(frame2, text=explcacion_tipos_NR3, bg="black", fg="green")
    texto_NR4 = tkinter.Label(frame2, text=explcacion_tipos_NR4, bg="black", fg="green")

    texto_NR1.pack(side="top")
    texto_NR2.pack(side="top")
    texto_NR3.pack(side="top")
    texto_NR4.pack(side="top")
    volver_boton_PWR.pack(side="top")
    



def intro11():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
    NR_boton.pack_forget()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame.winfo_children():
        widget.destroy()
    titulo2 = tkinter.Label(frame2, text="Centrals nuclears", bg="black", fg="green")
    titulo2.config(font=("arial", 50))
    intro = tkinter.Label(frame2, text="Hola!, Les centrals nuclears son maquines increibles amb una gran capacitat de producció, el seu funcionament es com una central termica convencional", bg="black", fg="green")
    titulo2.pack()
    intro.pack()

    intro.after(0, intro22())

  
def intro22():
    intro2 = tkinter.Label(frame2, text="pero amb un element mes, el reactor, un lloc on s'irradia neutrons a nuclis pesats (com urani o plutoni) per trencar el seus nuclis i produir energia", bg="black", fg="green")
    intro2.pack()
    intro2.after(0, intro33)

def intro33():
    intro3 = tkinter.Label(frame2, text="Vols saber mes? Pulsa un dels botons a baix per saber mes sobre les centrals nuclears", bg="black", fg="green")
    intro3.pack()
    
    
    partes.pack(side="top")
   
    tipos.pack(side="top")

    equipamiento.pack(side="top")

    Funcionamiento_boton.pack(side="top")



def pagp():

    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame.winfo_children():
        widget.destroy()
    volver_boton_Tipos.pack_forget()
    volver_boton_equipamiento_inicio.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
    NR_boton.pack_forget()
    ET.pack_forget()
    EC.pack_forget()
    ECon.pack_forget()
    ECom.pack_forget()
    EAux.pack_forget()
    Funcionamiento_boton.pack_forget()
    volver_boton_funcionamiento_inicio.pack_forget()
    titulo_pagp = tkinter.Label(frame2, text="QUE VOLS SABER?", bg="black", fg="darkgreen") #cambia el color a green cuando acabes
    titulo_pagp.config(font=("arial", 50))

    partes.pack(side="top")
    
   
    tipos.pack(side="top")
    titulo_pagp.pack(side="top")
    equipamiento.pack(side="top")
    Funcionamiento_boton.pack(side="top")


    
    
canvas = tkinter.Canvas(root, height=500, width=1000)
canvas.pack()


frame = tkinter.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)


frame2 = tkinter.Frame(root, bg="black")
frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


volver_boton_PWR = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=Tipos)
volver_boton_equipamiento = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=Equipamiento)
volver_boton_equipamiento_inicio = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=pagp)
volver_boton_funcionamiento_inicio = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=pagp)
volver_boton_Tipos = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=pagp)
PWR_boton = tkinter.Button(root, text="PWR", padx=10, pady=5, command=PWR)
BWR_boton = tkinter.Button(root, text="BWR", padx=10, pady=5, command=BWR)   #cambia el comando a bwr cuando lo tengas hecho
NR_boton = tkinter.Button(root, text="Neutrons rapids", padx=10, pady=5, command=NR)
partes = tkinter.Button(root, text="Parts", padx=10, pady=5, command=Partes)
tipos = tkinter.Button(root, text="Tipus", padx=10, pady=5, command=Tipos)
equipamiento = tkinter.Button(root, text="Equipament", padx=10, pady=5, command=Equipamiento)
EC = tkinter.Button(root, text="Edifici de contenció", padx=10, pady=5, command=EC) #cambia a EC cuando este hecho
ET = tkinter.Button(root, text="Edifici de tubines", padx=10, pady=5, command=ET) #cambia a ET cuando este hecho
ECom = tkinter.Button(root, text="Edifici de combustible", padx=10, pady=5, command=ECOM) #cambia a Ecom cuando este hecho
ECon = tkinter.Button(root, text="Edifici de control", padx=10, pady=5, command=ECOn) #cambia a ECon cuando este hecho            
EAux = tkinter.Button(root, text="Edifici auxiliar", padx=10, pady=5, command=EAUX) #cambia a EAux cuando este hecho
Funcionamiento_boton = tkinter.Button(root, text="Funcionament", padx=10, pady=5, command=Funcionamiento)
INICIO = tkinter.Button(frame, text="INICIO", padx=10, pady=5, command=intro11)
INICIO.pack(side="top")



root.mainloop()















    







