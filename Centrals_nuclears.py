import tkinter 
import time
from tkinter import filedialog, Text
import os
import sys
import PIL
from PIL import Image, ImageTk
import requests
from io import BytesIO
import time



m1 = int(500*0.8)
m2 = int(1000*0.8)

explicacion_partes1 = "-Vas del reactor: És un recipient on es produeix la fissió hi estan el combustible (urani o plutoni) i l'irradiador de neutrons, per trencar els nuclis"
explicacion_partes11 = "del combustible"
explicacion_partes2 = "-Moderador: Redueix la velocitat del neutrons, per assegurar la fissió i fer-la mes llarga, els moderadors mes utilitzats son l'aigua, l'aigua pesant"
explicacion_partes3 = "(format per atoms d'hidrogen amb 2 neutrons, mes conegut com deuteri) i el grafit"
explicacion_tipos_PWR1 = "Es el mes usat a nivell mundial, el refrigrant es impulsat per tot el vas i er l'intercambiador o generador de vapor, el pressionador fa que que l'aigua"
explicacion_tipos_PWR12 = "del refrigerador no entri en ebullició.El generador de vapor transfereix la calor del primer circuit al segon on l'aigua s'evapora i s'introdueix al"
explicacion_tipos_PWR13 = "reescalfador per eliminar l'humitat i així es converteix en vapor sec, i entra a la turbina on gracies a la pressió del gas la fa girar i produeix energia."
explicacion_tipos_PWR2 = "Despres de passar per la turbina, es va al condensador on torna a estat liquid i repeteix el procés."
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
    volver_boton_Tipos.pack(anchor=tkinter.E)

     
    titulo.pack(side="top")
    




def PWR():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
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
  
    
def intro11():
    volver_boton_Tipos.pack_forget()
    PWR_boton.pack_forget()
    BWR_boton.pack_forget()
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


    
canvas = tkinter.Canvas(root, height=500, width=1000)
canvas.pack()


frame = tkinter.Frame(root, bg="black")
frame.place(relwidth=0.95, relheight=0.95
)


frame2 = tkinter.Frame(root, bg="black")
frame2.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


volver_boton_PWR = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=Tipos)
volver_boton_Tipos = tkinter.Button(root, text="Torna enrere", padx=10, pady=5, command=intro11)
PWR_boton = tkinter.Button(root, text="PWR", padx=10, pady=5, command=PWR)
BWR_boton = tkinter.Button(root, text="BWR", padx=10, pady=5, command=PWR)   #cambia el comando a bwr cuando lo tengas hecho
partes = tkinter.Button(root, text="Partes", padx=10, pady=5, command=Partes)
tipos = tkinter.Button(root, text="Tipos", padx=10, pady=5, command=Tipos)


INICIO = tkinter.Button(frame, text="INICIO", padx=10, pady=5, command=intro11)
INICIO.pack(side="top")



root.mainloop()















    






