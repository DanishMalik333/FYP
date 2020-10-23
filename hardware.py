import time
import serial
ser1 = serial.Serial('COM6', 9600)
time.sleep(5)
ser1.write('256.1a'.encode())
time.sleep(5)
ser1.write('254.1'.encode())