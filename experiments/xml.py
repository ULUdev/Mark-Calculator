import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        #self.add_widget(Label(text="swanz"))
        self.add_widget(TextInput(multiline=False))
        self.add_widget(Button(text="mihihihi"))

class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    MyApp().run()