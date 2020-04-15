import time
import numpy
import matplotlib.pyplot as plt
import serial
 
ser = serial.Serial('COM3', 9600)

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