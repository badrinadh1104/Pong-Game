from kivy.app import App
from kivy.uix.widget import Widget
class pongBall(Widget):
    pass
class pongGame(Widget):
    pass
class pongApp(App):
    def build(self):
        return pongGame()
pongApp().run()