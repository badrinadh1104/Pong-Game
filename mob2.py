import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
class MyWork(Widget):
    name=ObjectProperty(None)
    lastname=ObjectProperty(None)
    def btn(self):
        print("name:",self.name.text,"lastname:",self.lastname.text )

class badriApp(App):
    def build(self):
        return MyWork()
badriApp().run()