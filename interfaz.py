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

#tinaco
tinaco=PhotoImage(file="./img/tinaco.gif")
imgTinaco=Label(canvas1, image=tinaco).place(x=0,y=100)

#boton llenado
fontExample2 = tkFont.Font(family="Arial", size=12)
seLlena=Button(canvas1,text="Llenar el tinaco",activebackground="#A9F5A9", font=fontExample2, bg="#642EFE", fg="white")#Agrego un botón con texto y llamo al método ledON que envía un 1 al arduino.
seLlena.config(width="15",height="2")#defino tamaño del botón
seLlena.place(x=80,y=430)#defino la ubicación del botón



ventana.mainloop()