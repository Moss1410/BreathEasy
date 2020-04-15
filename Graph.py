from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot, LinePlot, Plot
from kivy.clock import Clock
from threading import Thread
import time
import numpy
import matplotlib.pyplot as plt
import serial
from drawnow import *
import random
from sounds import *

clear = True
x_amount = 200

def get_microphone_level():
    global levels
    global pastLevels
    levels = []
    pastLevels = []
    try:
        ser = serial.Serial('COM3', 9600)
        while True:
            while (ser.inWaiting()==0):
                pass
            value = ser.readline()
            try:
                intValue = int(value.decode("utf-8"))
                update_level(intValue)
            except:
                pass
    except:
        while True:
            intValue = random.randint(1, 1020)
            update_level(intValue)
            time.sleep(0.01)

def update_level(value):
    global levels
    global pastLevels
    if len(levels) >= x_amount:
        pastLevels.append(levels.pop(0))
        if clear:
            pastLevels = levels.copy()
            levels = []
    if len(pastLevels) >= x_amount:
        pastLevels.pop(0)    
    levels.append(value)
    if value > 900:
        playSound(0)
    elif value < 100:
        playSound(1)

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = LinePlot(line_width=2.0, color=[0, 0, 1, 1])
        self.plot2 = LinePlot(line_width=1.5, color=[1, 0, 0, 0.6])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.add_plot(self.plot2)
        self.ids.graph.ymax=1023
        self.ids.graph.xmax=x_amount
        Clock.schedule_interval(self.get_value, 0.001)
        get_level_thread = Thread(target = get_microphone_level)
        get_level_thread.daemon = True
        get_level_thread.start()

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j) for i, j in enumerate(levels)]
        self.plot2.points = [(i, j) for i, j in enumerate(pastLevels)]
    
    def toggle(self):
        global clear
        clear = not clear


class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    
    RealTimeMicrophone().run()