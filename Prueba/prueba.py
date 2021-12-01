import serial#se importa la librería para conexión serial
import time#se importa librería de tiempos
from tkinter import *
from tkinter.font import Font

puerto=serial.Serial('COM3',9600)
time.sleep(1)
#puerto.open()

enviar_PIC=int(input("Inserte el numero para prender o apagar el LED. 69 para encender, 65 para apagar. 66 para salir\n"))
puerto.write(chr(enviar_PIC).encode())
time.sleep(1)

puerto.close()

#print(chr(enviar_PIC).encode())

