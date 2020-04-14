'''
Circle Example
==============

This example exercises circle (ellipse) drawing. You should see sliders at the
top of the screen with the Kivy logo below it. The sliders control the
angle start and stop and the height and width scales. There is a button
to reset the sliders. The logo used for the circle's background image is
from the kivy/data directory. The entire example is coded in the
kv language description.
'''

from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: 'vertical'

    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'BreathEasy Ventilator Control Panel'

    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e1
                min: -360.
                max: 360.
            Label:
                text: 'Breath Frequency (b/min) = {}'.format(e1.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e2
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'Inspiratory Pressure (cmH2O) = {}'.format(e2.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: e2
                min: -360.
                max: 360.
                value: 360
            Label:
                text: 'Inspiratory Time (s) = {}'.format(e2.value)

    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: wm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Pause Time (%/s) = {}'.format(wm.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: hm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Inspiratory Rise Time (s) = {}'.format(hm.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: hm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Cycle Threshold (%) = {}'.format(hm.value)

    BoxLayout:
        size_hint_y: None
        height: sp(100)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: wm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'Flow Trigger (L/min) = {}'.format(wm.value)
        BoxLayout:
            orientation: 'vertical'
            Slider:
                id: hm
                min: 0
                max: 2
                value: 1
            Label:
                text: 'FIO2 = {}'.format(hm.value)

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: sp(100)

        BoxLayout:
            size_hint_y: None
            height: sp(100)

            BoxLayout:
                id: graph1
                size_hint_y: None
                height: sp(100)
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
                size_hint_y: None
                height: sp(100)
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

        BoxLayout:
            size_hint_y: None
            height: sp(100)

            BoxLayout:
                id: graph3
                size_hint_y: None
                height: sp(100)
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
                size_hint_y: None
                height: sp(100)
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

    BoxLayout:
        size_hint_y: None
        height: 50
        Button:
            text: 'Reset Configuration'
            on_press: wm.value = 1; hm.value = 1;

'''


class CircleApp(App):
    def build(self):
        return Builder.load_string(kv)


CircleApp().run()



# FloatLayout:
#     canvas:
#         Color:
#             rgb: 1, 1, 1
#         Ellipse:
#             pos: 100, 100
#             size: 200 * wm.value, 201 * hm.value
#             source: 'data/logo/kivy-icon-512.png'
#             angle_start: e1.value
#             angle_end: e2.value