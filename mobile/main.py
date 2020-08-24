import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class Grid(Widget):
    pass

class designapp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    designapp().run()