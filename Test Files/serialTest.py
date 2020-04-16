import time
import numpy
import matplotlib.pyplot as plt
import serial
 
ser = serial.Serial('COM3', 9600)
mode = 2
if mode==1:
    while True:
        while (ser.inWaiting()==0):
            pass
        value = ser.readline()
        try:
            data = str(value.decode("utf-8"))
            data=data.split(",")
            signal1 = int(data[1])
            print(signal1)
        except:
            pass

elif mode==2:
    ser.write("Hello from Python!".encode())
    while True:
        data = ser.readline()
        if data:
            print(data.rstrip('\n'))