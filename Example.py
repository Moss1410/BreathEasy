import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        button = Button(text='Hello world!!!')
        button.text = "hi"
        print(button.text)
        return button


if __name__ == '__main__':
    MyApp().run()
