import serial#se importa la librería para conexión serial
import time#se importa librería de tiempos
from tkinter import * #importamos todos los métodos del paquete Tkinter para interfaz gráfica
import tkinter.font as tkFont
from tkinter import ttk

#creacion ventana
ventana=Tk()
ventana.title('Proyecto')
ventana.geometry("1200x1200")#Pone dimensiones a la ventana raíz ancho x alto
ventana.resizable(False,False)#condiciona si se puede o no agrandar la ventana con el mouse
ventana.iconbitmap("./img/escudoESCOM.ico")#agrega una imagen .ico a la ventana.

#fondo
background = PhotoImage(file = "./img/fondo1.png")
canvas1 = Canvas(ventana, width = 1200,height = 1200) 
canvas1.pack(fill = "both", expand = True)
# Desplegar imagen
canvas1.create_image( 0, 0, image = background, anchor = "nw")

#titulo
fontExample0 = tkFont.Font(family="Arial", size=16, weight="bold") #configuracion de la fuente
titulo=canvas1.create_text( 600, 20, text = "Proyecto Final de la materia de Instrumentación",font=fontExample0)

#subtitulo
fontExample1 = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic") #configuracion de la fuente
subtitulo=canvas1.create_text( 600, 45, text = "Equipo 12",font=fontExample1 )

fontExample2 = tkFont.Font(family="Arial", size=12)

#tinaco
tinaco=PhotoImage(file="./img/tinaco.gif")
tinacoLlenandose=PhotoImage(file="./img/tinacoLlenandose.gif")
tinacoLleno=PhotoImage(file="./img/tinacoLleno.gif")

Label(canvas1, image=tinaco, bg='white').place(x=0,y=100)

def llenandose():
    Label(canvas1,image=tinacoLlenandose, bg='white').place(x=0,y=100)
    llenando=Label(canvas1, text="Tinaco Llenandose...", font=fontExample2, borderwidth=2, relief="solid", bg='white').place(x=80,y=490)

def detener():
    Label(canvas1,image=tinacoLleno, bg='white').place(x=0,y=100)
    Label(canvas1, text="       Tinaco Lleno       ", font=fontExample2, borderwidth=2, relief="solid", bg='white').place(x=80,y=490)

Label(canvas1, text="  Faltan x metros para llenarse  ", font=fontExample2, bg="#F781F3").place(x=40,y=530)    
#boton llenado
seLlena=Button(canvas1,text="Llenar el tinaco",activebackground="#A9F5A9", font=fontExample2, bg="#642EFE", fg="white", command=llenandose)#Agrego un botón con texto y llamo al método ledON que envía un 1 al arduino.
seLlena.config(width="15",height="2")#defino tamaño del botón
seLlena.place(x=0,y=430)#defino la ubicación del botón

#boton lleno
parar=Button(canvas1,text="Detener llenado",activebackground="#A9F5A9", font=fontExample2, bg="#642EFE", fg="white", command=detener)#Agrego un botón con texto y llamo al método ledON que envía un 1 al arduino.
parar.config(width="15",height="2")#defino tamaño del botón
parar.place(x=150,y=430)#defino la ubicación del botón

#--------------------------------------------------------

#temperatura 
termometro=PhotoImage(file="./img/termometro.gif")
Label(canvas1, image=termometro, bg='white').place(x=400,y=100)
fontExample3 = tkFont.Font(family="Arial", size=28, weight="bold") 

Label(canvas1,text="La temperatura es de: ", font=fontExample2, bg='white').place(x=545,y=100)
Label(canvas1,text="X °C", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=590,y=125)

#--------------------------------------------------------

#luminosidad
foco=PhotoImage(file="./img/foco.gif")
Label(canvas1, image=foco, bg='white').place(x=750,y=100)

Label(canvas1,text="La luminosidad es del: ", font=fontExample2, bg='white').place(x=1000,y=100)
Label(canvas1,text="X %", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=1050,y=125)

#--------------------------------------------------------

#integrantes
Label(canvas1,text="Integrantes:\nGonzález Mora Erika Giselle\nHernández Rodríguez Armando Giovanni\nOlivares Ménez Gloria Oliva", font=fontExample2, bg='white').place(x=905,y=620)


ventana.mainloop()