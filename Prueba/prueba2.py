import serial#se importa la librería para conexión serial
import time#se importa librería de tiempos
from tkinter import *
from tkinter.font import Font

puerto=serial.Serial('COM3',9600)
time.sleep(1)
#puerto.open()

opc = True
while(opc):
    enviar_PIC=input("Inserte el numero para prender o apagar el LED. E para encender, A para apagar. S para salir\n")
    if(enviar_PIC != 'S'):
        puerto.write(enviar_PIC.encode())
        time.sleep(1)

    else:
        opc = False
        puerto.close()
        print("Puerto cerrado exitosamente")

#print(chr(enviar_PIC).encode())

