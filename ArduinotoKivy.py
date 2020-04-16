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
from drawnow import *
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
import data

# Our code file imports
import dataTransferStorage as dt
import inputScreen as inputScreen

clear = True
baudrate = 9600
graphTime = 10000 #number milliseconds

################################### GLOBAL FUNCTIONS ###################################
def get_data():
    global levels
    global times
    global oldLevels
    global oldTime
    global maxTime
    oldTime = []
    levels = []
    oldLevels = []
    times = []
    maxTime = 0
    try:
        ser = serial.Serial('COM3', baudrate)
        while True:
            while (ser.inWaiting()==0):
                pass
            value = ser.readline()
            try:
                data = str(value.decode("utf-8"))
                data=data.split(",")
                dataTime = int(data[0])
                signal1 = int(data[1])
                update_level(dataTime, signal1)
            except:
                pass
    except:
        currTime = 0
        while True:
            intValue = random.randint(1, 1020)
            currTime += 200
            update_level(currTime, intValue)
            time.sleep(0.1)

def update_level(timeIn, value):
    global levels
    global oldLevels
    global oldTime
    global times
    global maxTime
    timeIn -= maxTime
    if timeIn >= graphTime:
        maxTime +=timeIn
        oldLevels = levels.copy()
        oldTime = times.copy()
        levels = []
        times = []
        timeIn = 0
    levels.append(value)
    times.append(timeIn)

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

    #def update_all(self):


    def talk(self, message):
        print(message)

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
    
    def toggle(self):
        global clear
        clear = not clear

class Grapher(Graph):
    def __init__(self, **kwargs):
        super(Grapher, self).__init__(**kwargs)
        self.plot = LinePlot(line_width=2.0, color=[0, 0, 1, 1])
        self.plot2 = LinePlot(line_width=1.5, color=[1, 0, 0, 0.5])
        self.add_plot(self.plot)
        self.add_plot(self.plot2)
        self.ymax=1023
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
        get_level_thread = Thread(target = get_data)
        get_level_thread.daemon = True
        get_level_thread.start()
    
    def get_value(self, dt):
        self.plot.points = combineLists(times,levels)
        self.plot2.points = combineLists(oldTime,oldLevels)


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