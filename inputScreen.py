import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

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


kivy.require('1.9.0')  

Config.set('graphics', 'resizable', True)  

ventilatorModeDropDown = DropDown()
presetModeDropDown = DropDown()



class MyApp(App):

    # Setting buttons
    mandatoryBreath1= Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.55}, text="40")
    mandatoryBreath2= Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.42}, text="40")
    mandatoryBreath3= Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.29}, text="40")
    mandatoryBreath4= Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.16}, text="40")

    tiButton = Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.4, 'center_y':0.55}, text="40")
    tinspRiseButton = Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.4, 'center_y':0.42}, text="40")

    triggerButton = Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.6, 'center_y':0.55}, text="40")
    inspCycleRiseButton = Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.6, 'center_y':0.42}, text="40")

    psAbovePeepButton = Button(size_hint = (0.12, 0.08), pos_hint = {'center_x':0.8, 'center_y':0.55}, text="40")

    acceptButton= Button(size_hint = (0.1, 0.05), pos_hint = {'center_x':0.72, 'center_y':0.1}, text="ACCEPT")
    cancelButton= Button(size_hint = (0.1, 0.05), pos_hint = {'center_x':0.85, 'center_y':0.1}, text="CANCEL")

    def callback(self, event): 
   
        def on_text(instance, value):
            if(event == self.mandatoryBreath1):
                self.mandatoryBreath1.text = value
            elif(event == self.mandatoryBreath2):
                self.mandatoryBreath2.text = value
            elif(event == self.mandatoryBreath3):
                self.mandatoryBreath3.text = value
            elif(event == self.mandatoryBreath4):
                self.mandatoryBreath4.text = value
            elif (event == self.tiButton):
                self.tiButton.text = value
            elif (event == self.tinspRiseButton):
                self.tinspRiseButton.text = value
            elif (self.triggerButton == event):
                self.triggerButton.text = value
            elif (self.inspCycleRiseButton == event):
                self.inspCycleRiseButton.text = value
            else:
                self.psAbovePeepButton.text = value

            
        layout = GridLayout(cols = 1, padding = 10) 

        textinput = TextInput(multiline=False, text = '40')
        closeButton = Button(text = "OK") 

        layout.add_widget(textinput)      
        layout.add_widget(closeButton) 
    
        popup = Popup(title ='Please Enter the Value:', content = layout, size_hint =(None, None), size =(200, 150))   
        popup.open() 
        textinput.bind(text=on_text)
        closeButton.bind(on_press = popup.dismiss)

        

    def build(self):
     
        relativeLayout = RelativeLayout()

        # top title
        topTitle = Label(text='Set Ventilation Properties', pos_hint = {'center_x':0.5, 'center_y':0.95}, font_size = '50dp', bold = 'true')

        # setup the ventilator mode dropdown
        vcMode = Button(text="Volume Control", size_hint_y=None, height = 40)
        pcMode = Button(text="Pressure Control", size_hint_y=None, height = 40)
        vsMode = Button(text="Volume Support", size_hint_y=None, height = 40)
        psMode = Button(text="Pressure Support", size_hint_y=None, height = 40)
        bvMode = Button(text="Bi-vent", size_hint_y=None, height = 40)
        

        vcMode.bind(on_release = lambda btn: ventilatorModeDropDown.select(vcMode.text)) 
        pcMode.bind(on_release = lambda btn: ventilatorModeDropDown.select(pcMode.text)) 
        vsMode.bind(on_release = lambda btn: ventilatorModeDropDown.select(vsMode.text)) 
        psMode.bind(on_release = lambda btn: ventilatorModeDropDown.select(psMode.text)) 
        bvMode.bind(on_release = lambda btn: ventilatorModeDropDown.select(bvMode.text)) 
    
        ventilatorModeDropDown.add_widget(vcMode)
        ventilatorModeDropDown.add_widget(pcMode)
        ventilatorModeDropDown.add_widget(vsMode)
        ventilatorModeDropDown.add_widget(psMode)
        ventilatorModeDropDown.add_widget(bvMode)

        modeSelect = Button(size_hint = (0.15, 0.08), pos_hint = {'center_x':0.15, 'center_y':0.85}, text="Mode")
        modeSelect.bind(on_release = ventilatorModeDropDown.open)
        ventilatorModeDropDown.bind(on_select = lambda instance, x:setattr(modeSelect, 'text', x))

        # setup the presets dropdown
        presetMode1 = Button(text="Preset1", size_hint_y=None, height = 40)
        presetMode2 = Button(text="Preset2", size_hint_y=None, height = 40)
        presetMode3 = Button(text="Preset3", size_hint_y=None, height = 40)

        presetMode1.bind(on_release = lambda btn: presetModeDropDown.select(presetMode1.text)) 
        presetMode2.bind(on_release = lambda btn: presetModeDropDown.select(presetMode2.text)) 
        presetMode3.bind(on_release = lambda btn: presetModeDropDown.select(presetMode3.text)) 
    
        presetModeDropDown.add_widget(presetMode1)
        presetModeDropDown.add_widget(presetMode2)
        presetModeDropDown.add_widget(presetMode3)

        presetSelect = Button(size_hint = (0.15, 0.08), pos_hint = {'center_x':0.85, 'center_y':0.85}, text="Presets")
        presetSelect.bind(on_release = presetModeDropDown.open)
        presetModeDropDown.bind(on_select = lambda instance, x:setattr(presetSelect, 'text', x))

        # store preset button
        storePresetSelect = Button(size_hint = (0.15, 0.08), pos_hint = {'center_x':0.5, 'center_y':0.85}, text="Store Preselect")
        
        # Mandatory Breaths

        # top titles
        mandatoryBreathTitle = Label(text='Mandatory Breath', pos_hint = {'center_x':0.2, 'center_y':0.70}, font_size = '20dp', bold = "true")
        inspTimesTitle = Label(text='Insp. times', pos_hint = {'center_x':0.4, 'center_y':0.70}, font_size = '20dp', bold = "true")
        triggerTitle = Label(text='Trigger', pos_hint = {'center_x':0.6, 'center_y':0.70}, font_size = '20dp', bold = "true")
        supportBreathTitle = Label(text='Supported Breath', pos_hint = {'center_x':0.8, 'center_y':0.70}, font_size = '20dp', bold = "true")
        

        # bind button action
        self.mandatoryBreath1.bind(on_press = self.callback)
        self.mandatoryBreath2.bind(on_press = self.callback)
        self.mandatoryBreath3.bind(on_press = self.callback)
        self.mandatoryBreath4.bind(on_press = self.callback)
        self.tiButton.bind(on_press = self.callback)
        self.tinspRiseButton.bind(on_press = self.callback)
        self.triggerButton.bind(on_press = self.callback)
        self.inspCycleRiseButton.bind(on_press = self.callback)
        self.psAbovePeepButton.bind(on_press = self.callback)

        pcpeepLabel = Label(text = "PC above PEEP", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.61})
        simvLabel = Label(text = "SIMV Rate", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.48})
        peepLabel = Label(text = "PEEP", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.35})
        oxygenLabel = Label(text = "Oxygen Conc.", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.2, 'center_y':0.22})
        tiLabel = Label(text = "Ti", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.4, 'center_y':0.61})
        tiInspRiseLabel = Label(text = "T insp. rise", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.4, 'center_y':0.48})
        triggerLabel = Label(text = "Trigg. Flow", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.6, 'center_y':0.61})
        inspCycleRiseLabel = Label(text = "Insp. cycle off", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.6, 'center_y':0.48})
        psAbovePeepLabel = Label(text = "PS above PEEP", size_hint = (0.15, 0.08), pos_hint = {'center_x':0.8, 'center_y':0.61})

        # add widgets to the relative layout
        relativeLayout.add_widget(modeSelect)
        relativeLayout.add_widget(storePresetSelect)
        relativeLayout.add_widget(presetSelect)
        relativeLayout.add_widget(topTitle)
        relativeLayout.add_widget(mandatoryBreathTitle)
        relativeLayout.add_widget(inspTimesTitle)
        relativeLayout.add_widget(triggerTitle)
        relativeLayout.add_widget(supportBreathTitle)
        relativeLayout.add_widget(pcpeepLabel)
        relativeLayout.add_widget(simvLabel)
        relativeLayout.add_widget(peepLabel)
        relativeLayout.add_widget(oxygenLabel)
        relativeLayout.add_widget(tiLabel)
        relativeLayout.add_widget(tiInspRiseLabel)
        relativeLayout.add_widget(triggerLabel)
        relativeLayout.add_widget(inspCycleRiseLabel)
        relativeLayout.add_widget(psAbovePeepLabel)
        relativeLayout.add_widget(self.mandatoryBreath1)
        relativeLayout.add_widget(self.mandatoryBreath2)
        relativeLayout.add_widget(self.mandatoryBreath3)
        relativeLayout.add_widget(self.mandatoryBreath4)
        relativeLayout.add_widget(self.tiButton)
        relativeLayout.add_widget(self.tinspRiseButton)
        relativeLayout.add_widget(self.triggerButton)
        relativeLayout.add_widget(self.inspCycleRiseButton)
        relativeLayout.add_widget(self.psAbovePeepButton)
        relativeLayout.add_widget(self.acceptButton)
        relativeLayout.add_widget(self.cancelButton)

        relativeLayout.color = (0, 0, 0, 0)

        return relativeLayout


if __name__ == '__main__':
    MyApp().run()
