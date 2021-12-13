import serial#se importa la librería para conexión serial
import time#se importa librería de tiempos
from tkinter import * #importamos todos los métodos del paquete Tkinter para interfaz gráfica
import tkinter.font as tkFont
from tkinter import ttk

#creacion ventana principal
ventana=Tk()
ventana.title('Portada')
ventana.geometry("1200x1200")#Pone dimensiones a la ventana raíz ancho x alto
ventana.resizable(False,False)#condiciona si se puede o no agrandar la ventana con el mouse
ventana.iconbitmap("./img/escudoESCOM.ico")#agrega una imagen .ico a la ventana.

#fondo portada 
background0 = PhotoImage(file = "./img/fondo0.gif")
canvas0 = Canvas(ventana,width = 1200,height = 1200)
canvas0.pack(fill = "both", expand = True)
canvas0.create_image( 0, 0, image = background0, anchor = "nw")

#escudos 
ipn=PhotoImage(file="./img/ipn.gif")
escom=PhotoImage(file="./img/escom.gif")

Label(canvas0, image=ipn, bg='white').place(x=0,y=0)
Label(canvas0, image=escom, bg='white').place(x=1050,y=0)

#encabezados IPN y ESCOM
fontPrincipal0 = tkFont.Font(family="Delight Candles", size=20)
canvas0.create_text(600, 20, text = "Instituto Politécnico Nacional",font=fontPrincipal0)
canvas0.create_text(600, 80, text = "Escuela Superior de Cómputo",font=fontPrincipal0)

#equipo
fontPrincipal1 = tkFont.Font(family="Delight Candles", size=18)
canvas0.create_text(300, 230, text = "Equipo 12:\nGonzález Mora Erika Giselle\nHernández Rodríguez Armando Giovanni\nOlivares Ménez Gloria Oliva",font=fontPrincipal1)

#otros datos 
canvas0.create_text(950, 230, text ="Instrumentación\nProyecto Final\nProfra. Rocha Bernabe Rosario\n3CV13",font=fontPrincipal1)

#img nueva ventana
background = PhotoImage(file = "./img/fondo1.gif")
tinaco=PhotoImage(file="./img/tinaco.gif")
tinacoLlenandose=PhotoImage(file="./img/tinacoLlenandose.gif")
tinacoLleno=PhotoImage(file="./img/tinacoLleno.gif")
termometro=PhotoImage(file="./img/termometro.gif")
foco=PhotoImage(file="./img/foco.gif")

#funcion para crear nueva ventana
def nuevaVentana():
    newWindow=Toplevel(ventana)
    newWindow.title('Proyecto')
    newWindow.geometry("1200x1200")#Pone dimensiones a la ventana raíz ancho x alto
    newWindow.resizable(False,False)#condiciona si se puede o no agrandar la ventana con el mouse
    newWindow.iconbitmap("./img/escudoESCOM.ico")#agrega una imagen .ico a la ventana.
    #fondo
    canvas1 = Canvas(newWindow, width = 1200,height = 1200) 
    canvas1.create_image( 0, 0, image = background, anchor = "nw")
    canvas1.pack()

    #titulo
    fontExample0 = tkFont.Font(family="Arial", size=16, weight="bold") #configuracion de la fuente
    titulo=canvas1.create_text( 600, 20, text = "Proyecto Final de la materia de Instrumentación",font=fontExample0)
    #subtitulo
    fontExample1 = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic") #configuracion de la fuente
    subtitulo=canvas1.create_text( 600, 45, text = "Equipo 12",font=fontExample1 )

    fontExample2 = tkFont.Font(family="Arial", size=12)

        #tinaco
    Label(canvas1, image=tinaco, bg='white').place(x=0,y=100)
    Label(canvas1, text="       Tinaco Vacío      ", font=fontExample2, borderwidth=2, relief="solid", bg='white').place(x=80,y=490)
    distancia=Label(canvas1, text="  Faltan 100 cm para llenarse  ", font=fontExample2, bg="#F781F3")
    distancia.place(x=35,y=530)
    distancia.pack()

            #--------------------------------------------------------

            #temperatura 
    Label(canvas1, image=termometro, bg='white').place(x=400,y=100)
    fontExample3 = tkFont.Font(family="Arial", size=28, weight="bold") 
    Label(canvas1,text="La temperatura es de: ", font=fontExample2, bg='white').place(x=545,y=100)
    temperatura=Label(canvas1,text="X °C", font=fontExample3, borderwidth=2, relief="solid", bg='white')
    temperatura.place(x=590,y=125)
    temperatura.pack()

            #--------------------------------------------------------

            #luminosidad
    Label(canvas1, image=foco, bg='white').place(x=750,y=100)
    Label(canvas1,text="La luminosidad es del: ", font=fontExample2, bg='white').place(x=1000,y=100)
    luminosidad=Label(canvas1,text="X lux", font=fontExample3, borderwidth=2, relief="solid", bg='white')
    luminosidad.place(x=1050,y=125)    
    luminosidad.pack()

    #puerto serial
    puerto = serial.Serial('COM2',9600)
    time.sleep(1)
    print("Puerto abierto, listo para recibir datos")
    var = True
    while(var):
        lectura = puerto.readline().decode('ascii') # lo que leera del puerto (falta para llenarse)
        #print(lectura)
        #----tinaco
        if(lectura[1] == "d"):
            dist = float(lectura[2:7])
            distancia_nueva=StringVar()
            if(dist<=95.50):
                Label(canvas1,image=tinacoLlenandose, bg='white').place(x=0,y=100)
                Label(canvas1, text="Tinaco Llenandose...", font=fontExample2, borderwidth=2, relief="solid", bg='white').place(x=80,y=490)
                distancia_nueva.set("  Faltan "+str(dist)+ "cm para llenarse  ")
                distancia.config(textvariable=distancia_nueva)
                #Label(canvas1, text="  Faltan " + str(distancia) + "cm para llenarse  ", font=fontExample2, bg="#F781F3").place(x=35,y=530)
            elif(dist==0.01):
                Label(canvas1,image=tinacoLleno, bg='white').place(x=0,y=100)
                Label(canvas1, text="       Tinaco Lleno       ", font=fontExample2, borderwidth=2, relief="solid", bg='white').place(x=80,y=490)
                distancia_nueva.set("  Faltan "+str(dist)+ "cm para llenarse  ")
                distancia.config(textvariable=distancia_nueva)
                #Label(canvas1, text="  Faltan " + str(distancia) + "cm para llenarse  ", font=fontExample2, bg="#F781F3").place(x=35,y=530)
        #luminosidad
        elif(lectura[1] == "x"):
            luz = float(lectura[2:7])
            luz_nueva=StringVar()
            luz_nueva.set(str(luz)+"lux")
            luminosidad.config(textvariable=luz_nueva)
            #Label(canvas1,text=str(luz)+"lux", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=1050,y=125) 
        #temperatura 
        elif(lectura[1] == "t"):
            temp = float(lectura[2:7])
            tempNueva=StringVar()
            tempNueva.set(str(temp)+"°C")
            temperatura.config(textvariable=tempNueva)
            #Label(canvas1,text=str(temp)+"°C", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=590,y=125)
    puerto.close()

#boton ir a proyecto 
fontPrincipal2 = tkFont.Font(family="Montserrat", size=12)
ir=Button(canvas0,text="Vamos al proyecto",activebackground="#A4A4A4", font=fontPrincipal2, bg="black", fg="white", command=nuevaVentana)
ir.config(width="20",height="2")
ir.place(x=490,y=350)

ventana.mainloop()
