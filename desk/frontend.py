import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import backend as bck
Config.set("graphics", "width", "300")
Config.write()
class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 5
        self.selector = Spinner(
            text="average",
            values=("new subject", "new mark", "average"),
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.button = Button(
            text="swaaw",
            size_hint=(None, None),
            size=(500, 44)
        )
        self.button.bind(on_press=bck.pressed)
        self.input = TextInput(
            size_hint=(None, None),
            size=(500, 30),
            hint_text="Subject",
            multiline=False
        )
        self.input.bind(on_text_validate=bck.textchanged)
        self.add_widget(self.input)
        self.add_widget(self.button)
        self.add_widget(self.selector)


class app(App):
    def build(self):
        return Grid()
