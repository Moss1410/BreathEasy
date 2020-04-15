"""Real time plotting of Microphone level using kivy
"""

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
from datetime import datetime

clear = False
x_amount = 200

def get_microphone_level():
    global levels
    try:
        ser = serial.Serial('COM3', 9600)
        while True:
            while (ser.inWaiting()==0):
                pass
            value = ser.readline()
            try:
                intValue = int(value.decode("utf-8"))
                if len(levels) >= x_amount:
                    if clear:
                        levels = []
                    else:
                        levels.pop(0)
                levels.append(intValue)
            except:
                pass
    except:
        while True:
            intValue = random.randint(1, 1020)
            if len(levels) >= x_amount:
                if clear:
                    levels = []
                else:
                    levels.pop(0)
            levels.append(intValue)
            time.sleep(0.01)

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = LinePlot(line_width=2, color=[0, 0, 1, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
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

class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    
    RealTimeMicrophone().run()