from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.garden.graph import LinePlot
from kivy.clock import Clock
from threading import Thread

import time
import numpy
import serial
baudrate = 9600
graphTime = 10000 #number milliseconds

import random

def adjust(list,value):
    adjustedList = []
    for item in list:
        adjustedList.append(item-value)
    return adjustedList

def get_microphone_level():
    global levels
    global time
    global oldLevels
    global oldTime
    global max
    oldLevels = []
    oldTime = []
    ser = serial.Serial('COM3', baudrate)
    while True:
        while (ser.inWaiting()==0):
            pass
        value = ser.readline()
        try:
            data = str(value.decode("utf-8"))
            data=data.split(",")
            dataTime = int(data[0])-max
            signal1 = int(data[1])
            if dataTime >= graphTime:
                max=dataTime+max
                oldLevels=levels
                levels=[signal1]
                oldTime=time
                time=[0]
            else:
                levels.append(signal1)
                time.append(dataTime)
            # intValue = int(value.decode("utf-8"))
            # if len(levels) >= 2000:
            #     levels.pop(0)
            # levels.append(intValue)
        except:
            pass
    # try:
    #     ser = serial.Serial('COM3', baudrate)
    #     while True:
    #         while (ser.inWaiting()==0):
    #             pass
    #         value = ser.readline()
    #         try:
    #             data = str(value.decode("utf-8"))
    #             data.split(",")
    #             print(data.type())
    #             #data[-1]=int(data[-1])
    #             print(data)
    #             time = int(data[0])
    #             signal1 = int(data[1])
    #             if len(levels) >= graphTime:
    #                 oldLevels=levels
    #                 levels=[]
    #             #levels.append(intValue)
    #             # intValue = int(value.decode("utf-8"))
    #             # if len(levels) >= 2000:
    #             #     levels.pop(0)
    #             # levels.append(intValue)
    #         except:
    #             pass
    # except :
    #     while True:
    #         intValue = random.randint(1, 1020)
    #         if len(levels) >= graphTime:
    #             levels.pop(0)
    #         levels.append(intValue)
    #         time.sleep(0.01)


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
        self.plot = LinePlot(line_width=2.5, color=[0, 0, 1, 1])
        self.plot2 = LinePlot(line_width=1.5, color=[1, 0, 0, 0.5])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.add_plot(self.plot2)
        self.ids.graph.ymax=1023
        self.ids.graph.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = combineLists(time,levels)
        self.plot2.points = combineLists(oldTime,oldLevels)
class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    time = []
    max = 0
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimeMicrophone().run()