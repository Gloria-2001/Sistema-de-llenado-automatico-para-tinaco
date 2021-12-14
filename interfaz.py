import serial  # se importa la librería para conexión serial
import time  # se importa librería de tiempos
# importamos todos los métodos del paquete Tkinter para interfaz gráfica
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import threading
import sys
# creacion ventana principal
ventana = Tk()
ventana.title('Portada')
# Pone dimensiones a la ventana raíz ancho x alto
ventana.geometry("1200x1200")
# condiciona si se puede o no agrandar la ventana con el mouse
ventana.resizable(False, False)
# agrega una imagen .ico a la ventana.
ventana.iconbitmap("./img/escudoESCOM.ico")

# fondo portada
background0 = PhotoImage(file="./img/fondo0.gif")
canvas0 = Canvas(ventana, width=1200, height=1200)
canvas0.pack(fill="both", expand=True)
canvas0.create_image(0, 0, image=background0, anchor="nw")

# escudos
ipn = PhotoImage(file="./img/ipn.gif")
escom = PhotoImage(file="./img/escom.gif")

Label(canvas0, image=ipn, bg='white').place(x=0, y=0)
Label(canvas0, image=escom, bg='white').place(x=1050, y=0)

# encabezados IPN y ESCOM
fontPrincipal0 = tkFont.Font(family="Delight Candles", size=20)
canvas0.create_text(
    600, 20, text="Instituto Politécnico Nacional", font=fontPrincipal0)
canvas0.create_text(
    600, 80, text="Escuela Superior de Cómputo", font=fontPrincipal0)

# equipo
fontPrincipal1 = tkFont.Font(family="Delight Candles", size=18)
canvas0.create_text(
    300, 230, text="Equipo 12:\nGonzález Mora Erika Giselle\nHernández Rodríguez Armando Giovanni\nOlivares Ménez Gloria Oliva", font=fontPrincipal1)

# otros datos
canvas0.create_text(
    950, 230, text="Instrumentación\nProyecto Final\nProfra. Rocha Bernabe Rosario\n3CV13", font=fontPrincipal1)

# img nueva ventana
background = PhotoImage(file="./img/fondo1.gif")
tinaco = PhotoImage(file="./img/tinaco.gif")
tinacoLlenandose = PhotoImage(file="./img/tinacoLlenandose.gif")
tinacoLleno = PhotoImage(file="./img/tinacoLleno.gif")
termometro = PhotoImage(file="./img/termometro.gif")
foco = PhotoImage(file="./img/foco.gif")


def funcion(canvas1, distancia, luminosidad, temperatura, fontExample2, fontExample3):
    # puerto serial
    puerto = serial.Serial('COM2', 9600)
    time.sleep(1)
    print("Puerto abierto, listo para recibir datos")
    # var = True
    while(True):
        # lo que leera del puerto (falta para llenarse)
        lectura = puerto.readline().decode('ascii')
        print(lectura)
        # ----tinaco
        if(lectura[1] == "d"):
            dist = float(lectura[2:7])
            distancia_nueva = StringVar()
            if(dist <= 95.50):
                imgTinacoLlenando=Label(canvas1, image=tinacoLlenandose, bg='white')
                imgTinacoLlenando.pack()
                imgTinacoLlenando.place(x=0, y=100)

                textTinacoLlenando=Label(canvas1, text="Tinaco Llenandose...", font=fontExample2, borderwidth=2, relief="solid", bg='white')
                textTinacoLlenando.pack()
                textTinacoLlenando.place(x=80, y=490)

                distancia_nueva.set("  Faltan "+str(dist) + "cm para llenarse  ")
                distancia.config(textvariable=distancia_nueva)
                #Label(canvas1, text="  Faltan " + str(distancia) + "cm para llenarse  ", font=fontExample2, bg="#F781F3").place(x=35, y=530)
                if(dist == 0.01):
                    imgTinacoLleno=Label(canvas1, image=tinacoLleno,bg='white')
                    imgTinacoLleno.pack()
                    imgTinacoLleno.place(x=0, y=100)

                    textTinacoLleno=Label(canvas1, text="       Tinaco Lleno       ", font=fontExample2, borderwidth=2, relief="solid", bg='white')
                    textTinacoLleno.pack()
                    textTinacoLleno.place(x=80, y=490)

                    distancia_nueva.set("  Faltan 0 cm para llenarse  ")
                    distancia.config(textvariable=distancia_nueva)
                    #Label(canvas1, text="  Faltan " + str(distancia) + "cm para llenarse  ", font=fontExample2, bg="#F781F3").place(x=35, y=530)
        # luminosidad
        elif(lectura[1] == "x"):
            luz = float(lectura[2:7])
            luzNueva = StringVar()
            luzNueva.set(""+str(luz)+" lux")
            luminosidad.config(textvariable=luzNueva)
            #Label(canvas1, text=str(luz)+"lux", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=1050,y=125)
        # temperatura
        elif(lectura[1] == "t"):
            temp = float(lectura[2:7])
            tempNueva = StringVar()
            tempNueva.set(""+str(temp)+" °C")
            temperatura.config(textvariable=tempNueva)
            #Label(canvas1, text=str(temp)+"°C", font=fontExample3, borderwidth=2, relief="solid", bg='white').place(x=590,y=125)
    puerto.close()

# funcion para crear nueva ventana

def nuevaVentana():
    newWindow = Toplevel(ventana)
    newWindow.title('Proyecto')
    # Pone dimensiones a la ventana raíz ancho x alto
    newWindow.geometry("1200x1200")
    # condiciona si se puede o no agrandar la ventana con el mouse
    newWindow.resizable(False, False)
    # agrega una imagen .ico a la ventana.
    newWindow.iconbitmap("./img/escudoESCOM.ico")
    # fondo
    canvas1 = Canvas(newWindow, width=1200, height=1200)
    canvas1.create_image(0, 0, image=background, anchor="nw")
    canvas1.pack(fill="both", expand=True)
    # titulo
    # configuracion de la fuente
    fontExample0 = tkFont.Font(family="Arial", size=16, weight="bold")
    titulo = canvas1.create_text(600, 20, text="Proyecto Final de la materia de Instrumentación", font=fontExample0)
    # subtitulo
    # configuracion de la fuente
    fontExample1 = tkFont.Font(family="Arial", size=14, weight="bold", slant="italic")
    subtitulo = canvas1.create_text(600, 45, text="Equipo 12", font=fontExample1)

    fontExample2 = tkFont.Font(family="Arial", size=12)

    # tinaco
    imgTinacoVacio=Label(canvas1, image=tinaco, bg='white')
    imgTinacoVacio.pack()
    imgTinacoVacio.place(x=0, y=100)

    textoTinacoVacio=Label(canvas1, text="       Tinaco Vacío      ", font=fontExample2, borderwidth=2, relief="solid", bg='white')
    textoTinacoVacio.pack()
    textoTinacoVacio.place(x=80, y=490)
    
    distancia = Label(canvas1, text="  Faltan 100 cm para llenarse  ", font=fontExample2, bg="#F781F3")
    distancia.pack()
    distancia.place(x=35, y=530)

    # --------------------------------------------------------

    # temperatura
    imgTemp=Label(canvas1, image=termometro, bg='white')
    imgTemp.pack()
    imgTemp.place(x=400, y=100)

    fontExample3 = tkFont.Font(family="Arial", size=28, weight="bold")

    textTemp=Label(canvas1, text="La temperatura es de: ", font=fontExample2, bg='white')
    textTemp.pack()
    textTemp.place(x=545, y=100)
    
    temperatura = Label(canvas1, text="X °C", font=fontExample3, borderwidth=2, relief="solid", bg='white')
    temperatura.pack()
    temperatura.place(x=545, y=125)

    # --------------------------------------------------------

    # luminosidad
    imgLum=Label(canvas1, image=foco, bg='white')
    imgLum.pack()
    imgLum.place(x=750, y=100)

    textLum=Label(canvas1, text="La luminosidad es del: ", font=fontExample2, bg='white')
    textLum.pack()
    textLum.place(x=1000, y=100)

    luminosidad = Label(canvas1, text="X lux", font=fontExample3, borderwidth=2, relief="solid", bg='white')
    luminosidad.pack()
    luminosidad.place(x=1000, y=125)

    m_hilo = threading.Thread(target=funcion, args=(canvas1, distancia, luminosidad, temperatura, fontExample2, fontExample3),daemon=True)
    m_hilo.start()


# boton ir a proyecto
fontPrincipal2 = tkFont.Font(family="Montserrat", size=12)
ir = Button(canvas0, text="Vamos al proyecto", activebackground="#A4A4A4", font=fontPrincipal2, bg="black", fg="white", command=nuevaVentana)
ir.config(width="20", height="2")
ir.place(x=490, y=350)


def doSomething():
    ventana.destroy()
    #sys.exit()


ventana.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window

ventana.mainloop()
