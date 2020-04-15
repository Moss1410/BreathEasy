"""Real time plotting of Microphone level using kivy
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from kivy.core.window import Window
from threading import Thread
# import audioop
# import pyaudio

import time
import numpy
import matplotlib.pyplot as plt
import serial
from drawnow import *
import random


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
                #intValue = randInt(0, 1023)
                if len(levels) >= 2000:
                    levels.pop(0)
                levels.append(intValue)
            except:
                pass
    except:
        while True:
            intValue = random.randint(1, 1020)
            if len(levels) >= 2000:
                levels.pop(0)
            levels.append(intValue)
            time.sleep(0.01)


class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[0, 0, 1, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.ymax=1023
        self.ids.graph.xmax=2000
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j) for i, j in enumerate(levels)]

class RealTimeMicrophone(App):
    def build(self):
        Window.clearcolor = (0.07, 0.37, 0.55, 1)
        return Builder.load_file("alex.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimeMicrophone().run()