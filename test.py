import tkinter 
import time
from tkinter import filedialog, Text
import os
m1 = int(500 * 0.8)
m2 = int(1000 * 0.8)
explicacion_partes1 = "-Vas del reactor: És un recipient on es produeix la fissió hi estan el combustible (urani o plutoni) i l'irradiador de neutrons, per trencar els nuclis"
explicacion_partes11 = "del combustible"
explicacion_partes2 = "-Moderador: Redueix la velocitat del neutrons, per assegurar la fissió i fer-la mes llarga, els moderadors mes utilitzats son l'aigua, l'aigua pesant"
explicacion_partes3 = "(format per atoms d'hidrogen amb 2 neutrons, mes conegut com deuteri) i el grafit"
root = tkinter.Tk()

def Partes():
    texto_en_pantala = tkinter.Label(frame, text=explicacion_partes1, bg="grey")
    texto_en_pantala2 = tkinter.Label(frame, text=explicacion_partes11, bg="grey")
    texto_en_pantala3 = tkinter.Label(frame, text=explicacion_partes2, bg="grey")
    texto_en_pantala4 = tkinter.Label(frame, text=explicacion_partes3, bg="grey")
    
    print("pulsado")
    texto_en_pantala.pack(side="top")
    texto_en_pantala2.pack(side="top")
    texto_en_pantala3.pack(side="top")
    texto_en_pantala4.pack(side="top")


    
    



canvas = tkinter.Canvas(root, height=500, width=1000)
canvas.pack()

frame = tkinter.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

partes = tkinter.Button(frame, text="Partes", padx=10, pady=5, command=Partes)
partes.pack()

Tipos = tkinter.Button(frame, text="Tipos", padx=10, pady=5)
Tipos.pack()

root.mainloop()


