import time
import numpy
import matplotlib.pyplot as plt
import serial
from drawnow import *
 
potData = []
ser = serial.Serial('COM3', 9600)
plt.ion()

def makeFig():
    plt.ylim(0, 1023)
    plt.title('Potentiometer Data')
    plt.grid(True)
    plt.ylabel('Potentiometer Value')
    plt.plot(potData, 'ro-', label='Potentiometer Values')
 
while True:
    while (ser.inWaiting()==0):
        pass
    value = ser.readline()
    intValue = int(value.decode("utf-8"))
    potData.append(intValue)
    drawnow(makeFig)