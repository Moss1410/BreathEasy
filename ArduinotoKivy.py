from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot, LinePlot, Plot, Graph
from kivy.clock import Clock
from kivy.core.window import Window
from threading import Thread
import time
import numpy
import matplotlib.pyplot as plt
import serial
from drawnow import *
import random
from sounds import *

#peakPressure
#respirationRate
#tidalVolume

sim = True
import dataTransferStorage as dt

clear = True
baudrate = 9600
graphTime = 10000 #number milliseconds


import csv
def getSim1():
    global data1
    data1={}
    with open('sineWaveExample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
           data1[float(row[0])]=float(row[1])


def get_data():
    global data1



    global times
    global peakPressure
    global oldpeakPressure
    global respirationRate
    global oldrespirationRate
    global oldTime
    global maxTime
    oldTime = []
    peakPressure = []
    oldpeakPressure = []
    respirationRate = []
    oldrespirationRate = []
    times = []
    maxTime = 0
    ser = serial.Serial('COM3', baudrate)
    try:
        while True:
            while (ser.inWaiting()==0):
                pass
            value = ser.readline()
            try:
                data = str(value.decode("utf-8"))
                data=data.split(",")
                dataTime = int(data[0])
                signal0 = 500
                signal1 = int(data[1])
                update_level(dataTime, signal0, signal1)
                update_sim1(dataTime)
            except:
                pass
    except:
        currTime = 0
        while True:
            intValue = random.randint(1, 1020)
            currTime += 200
            update_level(currTime, 500, intValue)
            time.sleep(0.1)

def update_level(timeIn, value0, value):
    global peakPressure
    global oldpeakPressure
    global respirationRate
    global oldrespirationRate
    global oldTime
    global times
    global maxTime
    timeIn -= maxTime
    if timeIn >= graphTime:
        maxTime += timeIn
        oldTime = times.copy()
        oldpeakPressure = peakPressure.copy()
        oldrespirationRate = respirationRate.copy()
        peakPressure = []
        respirationRate = []
        times = []
        timeIn = 0
    times.append(timeIn)
    peakPressure.append(value0)
    respirationRate.append(value)

def combineLists(list1,list2):
    list=[]
    index=0
    for v in list1:
        list.append((list1[index],list2[index]))
        index+=1
    return list

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
    
    def toggle(self):
        global clear
        clear = not clear

class Grapher(Graph):
    def __init__(self, **kwargs):
        super(Grapher, self).__init__(**kwargs)
        self.respirationRate = LinePlot(line_width=2.0, color=[0, 0, 1, 1])
        self.oldrespirationRate = LinePlot(line_width=1.5, color=[1, 0, 0, 0.5])
        self.add_plot(self.respirationRate)
        self.add_plot(self.oldrespirationRate)
        self.ymax=1023
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
        get_level_thread = Thread(target = get_data)
        get_level_thread.daemon = True
        get_level_thread.start()
    
    def get_value(self, dt):
        self.respirationRate.points = combineLists(times,respirationRate)
        self.oldrespirationRate.points = combineLists(oldTime,oldrespirationRate)

class BreathEasy(App):
    def build(self):
        Window.clearcolor = (0.07, 0.37, 0.55, 1)
        return Builder.load_file("alex.kv")

if __name__ == "__main__":
    getSim1()
    dt.make_setttings_default()
    dt.create_settings_string()
    dt.interpret_input()
    BreathEasy().run()