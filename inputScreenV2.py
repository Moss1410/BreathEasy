import kivy
from kivy.app import App
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

kivy.require('1.0.7')

Config.set('graphics', 'resizable', True) 

class TestApp(App):
    pass


if __name__ == '__main__':
    TestApp().run()