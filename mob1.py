import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=1
        self.inside = GridLayout()
        self.inside.cols = 2


        self.inside.add_widget(Label(text="name"))
        self.name=TextInput(multiline=False)
        self.inside.add_widget(self.name)


        self.inside.add_widget(Label(text="lastname"))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)


        self.submit=Button(text="submit",font_size=45)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.add_widget(self.inside)


    def pressed(self,instance):
        name=self.name.text
        lastname=self.lastname.text
        print("name:",name ,"\n","lastname :",lastname)
        print("pressed")

class MyApp(App):
    def build(self):
        return MyGrid()
MyApp().run()