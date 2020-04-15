from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    id: root_box
    spacing: 5
    orientation: 'vertical'

    # TITLE PANEL
    Label:
        size_hint: 1, 0.1
        text: 'BreathEasy Ventilator Control Panel'


    # SLIDERS 1
    BoxLayout:
        size_hint: 1, 0.10
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_1
                min: -360.
                max: 360.
            Label:
                text: 'Breath Frequency (b/min) = {}'.format(parameter_1.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_2
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'Inspiratory Pressure (cmH2O) = {}'.format(parameter_2.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_3
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'Inspiratory Time (s) = {}'.format(parameter_2.value)

    # SLIDERS 2
    BoxLayout:
        size_hint: 1, 0.10
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_4
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Pause Time (%/s) = {}'.format(parameter_3.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_5
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Inspiratory Rise Time (s) = {}'.format(parameter_4.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_6
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Cycle Threshold (%) = {}'.format(parameter_4.value)

    # SLIDERS 3
    BoxLayout:
        size_hint: 1, 0.10
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_7
                min: 0
                max: 10
                value: 0
            Label:
                text: 'Flow Trigger (L/min) = {}'.format(parameter_7.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: parameter_8
                min: 0
                max: 10
                value: 0
            Label:
                text: 'FIO2 = {}'.format(parameter_8.value)

    # GRAPHS PANEL
    BoxLayout:
        spacing: 5
        orientation: 'vertical'
        size_hint: 1, 0.55

        # GRAPH PAIR 1
        BoxLayout:
            size_hint: 1, 0.25
            spacing: 5

            BoxLayout:
                id: graph1
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: None
                    height: sp(100)
                    canvas:
                        Color:
                            rgb: 1, 0, 0
                        Rectangle:
                            pos: graph1.pos[0], graph1.pos[1]
                            size: graph1.width, graph1.height

            BoxLayout:
                id: graph2
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: None
                    height: sp(100)
                    canvas:
                        Color:
                            rgb: 0, 1, 0
                        Rectangle:
                            pos: graph2.pos[0], graph2.pos[1]
                            size: graph2.width, graph2.height

        # GRAPH PAIR 2
        BoxLayout:
            size_hint: 1, 0.25
            spacing: 5

            BoxLayout:
                id: graph3
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: None
                    height: sp(100)
                    canvas:
                        Color:
                            rgb: 0, 0, 1
                        Rectangle:
                            pos: graph3.pos[0], graph3.pos[1]
                            size: graph3.width, graph3.height

            BoxLayout:
                id: graph4
                orientation: 'vertical'
                BoxLayout:
                    size_hint_y: None
                    height: sp(100)
                    canvas:
                        Color:
                            rgb: 1, 1, 0
                        Rectangle:
                            pos: graph4.pos[0], graph4.pos[1]
                            size: graph4.width, graph4.height

    # RESET BUTTON PANEL
    BoxLayout:
        size_hint_y: None
        size_hint: 1, 0.05
        Button:
            text: 'Reset Configuration'
            on_press: parameter_1.value = 0; parameter_2.value = 0; parameter_3.value = 1; parameter_4.value = 1; parameter_5.value = 0; parameter_6.value = 0; parameter_7.value = 0; parameter_8.value = 0;
'''


class DashBoardApp(App):
=======

'''


class CircleApp(App):
    def build(self):
        return Builder.load_string(kv)


DashBoardApp().run()

