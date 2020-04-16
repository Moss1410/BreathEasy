import time

import serial

ser = serial.Serial('COM3', 9600)



 
while True:
 value = ser.readline()
 a = value.decode("utf-8")
 b = int(a)
 print(b)
 time.sleep(0.00001)
   