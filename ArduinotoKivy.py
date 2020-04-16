# External library imports
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot, LinePlot, Plot, Graph
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from threading import Thread
import time
import numpy
import matplotlib.pyplot as plt
import serial
import random
from sounds import *
import kivy
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown 
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout 
from kivy.config import Config  
from kivy.base import runTouchApp 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.popup import Popup  
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle 
from kivy.properties import StringProperty

import data
from scipy import integrate


#peakPressure
#respirationRate
#tidalVolume

# Our code file imports
import dataTransferStorage as dt
import inputScreen as inputScreen

clear = True
baudrate = 9600
graphTime = 10000 #number milliseconds
oldTime = []
peakPressure = []
oldpeakPressure = []
tidalVolume = []
oldtidalVolume = []
respirationRate = []
oldrespirationRate = []
times = []
RR = 0

corrupt=True


import csv

def getCurve(file):
    dictionary = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
           dictionary[float(row[0])]=float(row[1])
    return dictionary
        
data1=getCurve('SquareWave.csv')
data2=getCurve('FlowWave.csv')

global incomings
incomings = data.IncomingDatas()



################################### GLOBAL FUNCTIONS ###################################
def get_data():
    global data1
    global times
    global tidalVolume
    global oldtidalVolume
    global peakPressure
    global oldpeakPressure
    global respirationRate
    global oldrespirationRate
    global oldTime
    global maxTime
    global corrupt
    maxTime = 0
    startingTime=time.time()
    while (corrupt and (int(time.time()-startingTime)<=1)):
        try: 
            ser = serial.Serial('COM3', baudrate)
            corrupt=False
            while True:
                while (ser.inWaiting()==0):
                    pass
                value = ser.readline()
                try:
                    data = str(value.decode("utf-8"))
                    data=data.split(",")
                    dataTime = int(data[0])
                    signal0=0
                    signal1 = int(data[1])
                    update_level(dataTime, 0, signal1, 0)
                except:
                    pass
        except:
            pass
    if corrupt==True:
        currTime = 0
        while True:
            pp = data1[currTime/1000]
            rr = data2[currTime/1000]
            tv = 500
            if len(times)!=0:
                y_int = integrate.cumtrapz(times, peakPressure, initial=0)
            else:
                y_int = 0
            update_level(currTime, pp, rr, tv)
            currTime += 10
            time.sleep(0.01)

def update_level(timeIn, pp, rr, tv):
    global peakPressure
    global oldpeakPressure
    global respirationRate
    global oldrespirationRate
    global tidalVolume
    global oldtidalVolume

    global oldTime
    global times
    global maxTime
    timeIn -= maxTime
    if timeIn >= graphTime:
        maxTime += timeIn
        oldTime = times.copy()
        oldpeakPressure = peakPressure.copy()
        oldrespirationRate = respirationRate.copy()
        oldtidalVolume = tidalVolume.copy()
        peakPressure = []
        respirationRate = []
        tidalVolume=[]
        times = []
        timeIn = 0
    times.append(timeIn)
    #peakPressure.append(value0)
    peakPressure.append(pp)
    respirationRate.append(rr)
    tidalVolume.append(tv)

def combineLists(list1,list2):
    list=[]
    index=0
    for v in list1:
        list.append((list1[index],list2[index]))
        index+=1
    return list

################################### CLASSES (FOR KIVY) ###################################
class VButton(Button):
    def __init__(self, **kwargs):
        super(VButton, self).__init__(**kwargs)

    # button click function
    def callback(self):#, event): 
       
        # Setup the popup layout    
        layout = GridLayout(cols = 1, padding = 10) 
        print("\u2193")

        self.textinput = TextInput(multiline=False, text = '40')
        closeButton = Button(text = "OK") 

        layout.add_widget(self.textinput)      
        layout.add_widget(closeButton) 

        self.popup = Popup(title ='Please Enter the Value:', content = layout, size_hint =(None, None), size =(200, 150))   
        self.popup.open() 
        # textinput.bind(text=on_text)
        
        closeButton.bind(on_press = self.setValue)
    
    def setValue(self, send):
        self.popup.dismiss()
        global settings
        settings.__dict__[self.name].set_value(int(self.textinput.text))
        self.text = str(settings.__dict__[self.name].get_value())

    def talk(self, message):
        print(message)

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
    
    def toggle(self):
        global clear
        clear = not clear


class ChangeLabel(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs) 
        Clock.schedule_interval(self.update, 0.001)
        #print("hi")

    def update(self, dt):
        self.text = str(incomings.__dict__[self.name].get_value())


class PeakPressure(Graph):
    def __init__(self, **kwargs):
        super(PeakPressure, self).__init__(**kwargs)
        self.peakPressure = LinePlot(line_width=1.5, color=[1, 0, 0, 1])
        self.oldpeakPressure = LinePlot(line_width=1, color=[1, 0, 0, 0.2])
        self.add_plot(self.peakPressure)
        self.add_plot(self.oldpeakPressure)
        self.ymax=1023
        self.ymin=0
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
    
    def get_value(self, dt):
        self.peakPressure.points = combineLists(times,peakPressure)
        self.oldpeakPressure.points = combineLists(oldTime,oldpeakPressure)

class RespiratoryRate(Graph):
    def __init__(self, **kwargs):
        super(RespiratoryRate, self).__init__(**kwargs)
        self.respirationRate = LinePlot(line_width=1.5, color=[0, 0.5, 0, 1])
        self.oldrespirationRate = LinePlot(line_width=1, color=[0, 0.5, 0, 0.2])
        self.add_plot(self.respirationRate)
        self.add_plot(self.oldrespirationRate)
        self.ymax=900
        self.ymin=-900
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
        get_level_thread = Thread(target = get_data)
        get_level_thread.daemon = True
        get_level_thread.start()
    
    def get_value(self, dt):
        self.respirationRate.points = combineLists(times,respirationRate)
        self.oldrespirationRate.points = combineLists(oldTime,oldrespirationRate)
class TidalVolume(Graph):
    def __init__(self, **kwargs):
        super(TidalVolume, self).__init__(**kwargs)
        self.tidalVolume = LinePlot(line_width=1.5, color=[0, 0, 1, 1])
        self.oldtidalVolume = LinePlot(line_width=1, color=[0, 0, 1, 0.2])
        self.add_plot(self.tidalVolume)
        self.add_plot(self.oldtidalVolume)
        self.ymax=1023
        self.ymin=0
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
    
    def get_value(self, dt):
        self.tidalVolume.points = combineLists(times,tidalVolume)
        self.oldtidalVolume.points = combineLists(oldTime,oldtidalVolume)


################################### MAIN APP CLASS ###################################
class BreathEasy(App):
    def build(self):
        # Set the initial window color for our app
        Window.clearcolor = (0.07, 0.37, 0.55, 1)
        return Builder.load_file("total.kv")

################################### MAIN LOOP (RUNS APP) ###################################
if __name__ == "__main__":
    global settings
    
    settings = data.Settings()
    dt.make_setttings_default()
    dt.create_settings_string()
    dt.interpret_input()
    BreathEasy().run()