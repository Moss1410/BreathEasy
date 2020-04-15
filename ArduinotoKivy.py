"""Real time plotting of Microphone level using kivy
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread

import time
import numpy
import serial
ser = serial.Serial('COM3', 9600)
graphTime = 3000 #number datapoints? I'm not sure exactly

def get_microphone_level():
    """
    source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    audioop.max alternative to audioop.rms
    """
    
    global levels
    # while True:
    #     if (ser.inWaiting()==0):
    #         if len(levels)!=0:
    #             levels.append(levels[-1])
    #     value = ser.readline()
    #     try:
    #         intValue = int(value.decode("utf-8"))
    #         if len(levels) >= 2000:
    #             levels.pop(0)
    #         levels.append(intValue)
    #     except:
    #         pass

    while True:
        while (ser.inWaiting()==0):
            pass
        value = ser.readline()
        try:
            intValue = int(value.decode("utf-8"))
            if len(levels) >= graphTime:
                levels.pop(0)
            levels.append(intValue)
        except:
            pass

class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[0, 0, 1, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.ymax=1023
        self.ids.graph.xmax=graphTime
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j) for i, j in enumerate(levels)]

class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimeMicrophone().run()