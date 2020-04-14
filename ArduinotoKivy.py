"""Real time plotting of Microphone level using kivy
"""

from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread
# import audioop
# import pyaudio

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
 




def get_microphone_level():
    """
    source: http://stackoverflow.com/questions/26478315/getting-volume-levels-from-pyaudio-for-use-in-arduino
    audioop.max alternative to audioop.rms
    """
    # chunk = 1024
    # FORMAT = pyaudio.paInt16
    # CHANNELS = 1
    # RATE = 44100
    # p = pyaudio.PyAudio()

    # s = p.open(format=FORMAT,
    #            channels=CHANNELS,
    #            rate=RATE,
    #            input=True,
    #            frames_per_buffer=chunk)
    # global levels
    # while True:
    #     data = s.read(chunk)
    #     mx = audioop.rms(data, 2)
    #     if len(levels) >= 100:
    #         levels = []
    #     levels.append(mx)
    global levels
    while True:
        while (ser.inWaiting()==0):
            pass
        value = ser.readline()
        intValue = int(value.decode("utf-8"))
        if len(levels) >= 100:
            levels = []
        levels.append(intValue)
        



class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.001)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
        self.plot.points = [(i, j/5) for i, j in enumerate(levels)]

class RealTimeMicrophone(App):
    def build(self):
        return Builder.load_file("look.kv")

if __name__ == "__main__":
    levels = []  # store levels of microphone
    get_level_thread = Thread(target = get_microphone_level)
    get_level_thread.daemon = True
    get_level_thread.start()
    RealTimeMicrophone().run()