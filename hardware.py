import time
import serial
def ser_com(strng):
    ser1 = serial.Serial('COM3', 9600)

    ser1.write(strng.encode())
    ser1.close()
