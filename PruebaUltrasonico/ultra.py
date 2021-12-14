import serial
import time

puerto = serial.Serial('COM2',9600)
time.sleep(1)
print("Puerto abierto, listo para recibir datos")
var = True
while(var):
    x = puerto.readline().decode('ascii')
    print(x)

puerto.close()
