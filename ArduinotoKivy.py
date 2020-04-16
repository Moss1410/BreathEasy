from kivy.config import Config
Config.set('graphics', 'width', '1500') 
Config.set('graphics', 'height', '900')

# from kivy.config import Config
# Config.set('graphics', 'resizable', '0') 
# Config.set('graphics', 'width', '1700') 
# Config.set('graphics', 'height', '900')

# External library imports
#from kivy.config import Config
#Config.set('graphics', 'fullscreen', '1')

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
import statistics
import random

#peakPressure
#respirationRate
#tidalVolume

# Our code file imports

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
PEEP = 100000000000000

corrupt=True


import csv

def getCurve(file):
    dictionary = {}
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
           dictionary[float(row[0])]=float(row[1])
    return dictionary
        
data1=getCurve('SquareWave2.csv')
data2=getCurve('FlowWave.csv')
data3=getCurve('VolumeWave.csv')
data4=getCurve('zeroes.csv')



################################### GLOBAL FUNCTIONS ###################################

def get_data():
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
    global PEEP
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
                    signal1 = int(data[1])-500
                    update_level(dataTime, 0, signal1, 0)
                except:
                    pass
        except:
            pass
    if corrupt==True:
        currTime = 0.0
        while True:
            
            if currTime/1000 not in data1.keys():
                currTime = 0.0
                maxTime = 0
            pp = data1[currTime/1000]/30
            #pp=45
            rr = data2[currTime/1000]/12
            tv = data3[currTime/1000]/3
            update_level(currTime, pp, rr, tv)
            currTime += 10
            time.sleep(0.01)
            

def getRR():
    newRR=0
    average=statistics.mean(respirationRate)
    counter=0
    mode=1
    length=len(respirationRate)
    newRR=0
    maxTimes=[0]
    maxValues=[]
    tpv=graphTime/len(respirationRate) #time difference between each point of data
    times=[]
    for value in respirationRate:
        if mode == 1:
            startCounter = counter
            if value>=average+40:
                startCounter=counter
                mode = 2
                maxValues.append(value)
        elif mode == 2:
            if maxValues[newRR]<=value:
                maxValues[newRR]=value
            if (value<=average+20) and startCounter+10<counter:
                mode = 3
                newRR+=1
        elif mode == 3:
            if maxValues[newRR-1]<=value:
                maxValues[newRR-1]=value
            if value<=average-20:
                counter2=startCounter
                found = False
                while (counter2 < counter) and not found:
                    if respirationRate[counter2] == maxValues[-1]:
                        found = True
                        times.append(counter2*tpv)
                    counter2+=1
                mode=1
        if (counter-startCounter>length/2):
            startCounter=counter
        counter+=1
    newRR=60000/((max(times)-min(times))/(len(maxValues)-1))
    return newRR

def getPressureAverage():
    average1 = statistics.mean(peakPressure)
    return average1

def getPressurePeak():
    return max(peakPressure)

def getVolumePeak():
    return max(tidalVolume)

def getPEEP():
    average1 = statistics.mean(peakPressure)
    lowerHalf = []
    for value in peakPressure:
        if value < average1:
            lowerHalf.append(value)
    average2 = statistics.mean(lowerHalf)
    return average2

def update_level(timeIn, pp, rr, tv):
    global peakPressure
    global oldpeakPressure
    global respirationRate
    global oldrespirationRate
    global tidalVolume
    global oldtidalVolume
    global incomings

    incomings.time.set_value(timeIn)
    incomings.inspiratory_pressure.set_value(pp)
    incomings.inspiratory_flow.set_value(rr)
    incomings.tidal_volume.set_value(tv)
    if timeIn%500==0:
        incomings.voltage.set_value(24 + data4[timeIn/1000])
        incomings.Fi02.set_value(settings.FiO2.get_value() - data4[timeIn/1000])

    global oldTime
    global times
    global maxTime
    timeIn -= maxTime
    if timeIn >= graphTime:
        incomings.PEEP.set_value(round(getPEEP(),2))
        incomings.respiratory_rate.set_value(round(getRR(),2)) # this seems to give a constant value for some reason -Nick
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
<<<<<<< HEAD

=======
>>>>>>> origin/PleaseWorkThisTimebyNick
    # button click function
    def callback(self):#, event): 
       
        # Setup the popup layout    
        layout = GridLayout(cols = 1, padding = 10) 
        print("\u2193")

        self.textinput = TextInput(multiline=False, text = str(settings.__dict__[self.name].get_value()))
        closeButton = Button(text = "OK") 

        layout.add_widget(self.textinput)      
        layout.add_widget(closeButton) 

        self.popup = Popup(title ='Please Enter the Value:', content = layout, size_hint =(None, None), size =(200, 150))   
        self.popup.open() 
        # textinput.bind(text=on_text)
        
        closeButton.bind(on_press = self.setValue)
    
    def setValue(self, send):
        global settings
        try:
            float(self.textinput.text)
        except:
            self.textinput.text = "Try Again"
            return
        settings.__dict__[self.name].set_value(float(self.textinput.text))
        self.text = str(settings.__dict__[self.name].get_value())
        self.popup.dismiss()

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
        self.ymax=50
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
        self.ymax=60
        self.ymin=-60
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
        self.ymax=400
        self.ymin=0
        self.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)
    
    def get_value(self, dt):
        self.tidalVolume.points = combineLists(times,tidalVolume)
        self.oldtidalVolume.points = combineLists(oldTime,oldtidalVolume)


################################### MAIN APP CLASS ###################################
class BreathEasy(App):
    close = True

    def __init__(self, **kwargs):
        super(BreathEasy, self).__init__(**kwargs)
        self.che = True
        Window.bind(on_request_close=self.exit_check)
        # get_level_thread = Thread(target = self.show_warnings)
        # get_level_thread.daemon = True
        # get_level_thread.start()
    
    # def show_warnings(self):
    #     global warns
    #     warns.update_all_warning_status()
    #     lister = warns.get_warnings()
    #     for warn in lister:
    #         if warn.get_status() == 1 and self.che:
    #             self.che = False
    #             layout = GridLayout(cols = 1, padding = 10) 
    #             closeButton = Button(text = "Close") 

    #             layout.add_widget(closeButton) 

    #             self.popup = Popup(title = warn.get_name(), content = layout, size_hint =(None, None), size =(500, 500))   
    #             self.popup.open() 
    #             # textinput.bind(text=on_text)
                
    #             closeButton.bind(on_press = self.pops)

    def pops(self, somethings):
        self.popup.dismiss
        self.che = True

    def exit_check(self, *args):
        layout = GridLayout(cols = 1, padding = 10) 
        okButton = Button(text = 'OK')
        cancelButton = Button(text = "Cancel") 
        layout.add_widget(okButton)
        layout.add_widget(cancelButton) 
        popup = Popup(title ='Are you sure?', content = layout, size_hint =(None, None), size =(200, 150))
        popup.open() 
        cancelButton.bind(on_press = popup.dismiss)
        okButton.bind(on_press = self.closeApp)
        return self.close

    def closeApp(self, send):
        self.close = False
        Window.close()
    
    def build(self):
        # Set the initial window color for our app
        Window.clearcolor = (24/255, 24/255, 24/255, 1)
        return Builder.load_file("total.kv")

################################### MAIN LOOP (RUNS APP) ###################################
if __name__ == "__main__":
    global settings

    global incomings
    incomings = data.IncomingDatas()
    settings = data.Settings()
    global warns
    warns = data.Warnings(incomings, settings)
    
    
    BreathEasy().run()