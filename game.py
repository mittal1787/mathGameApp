import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.properties import DictProperty, ObjectProperty
from kivy.lang import Builder

class WindowManager(ScreenManager):
    group_dict = DictProperty({"A0": 0})

class OpenScreen(Screen):
    pass

class QuestionScreenOne(Screen):
    pass


class QuestionScreenTwo(Screen):
    pass


class QuestionScreenThree(Screen):
    pass

class QuestionScreenFour(Screen):
    pass

class QuestionScreenFive(Screen):
    pass

class QuestionScreenSix(Screen):
    pass

class QuestionScreenSeven(Screen):
    pass

class QuestionScreenEight(Screen):
    pass

class QuestionScreenNine(Screen):
    pass

class QuestionScreenTen(Screen):
    pass

class EndScreen(Screen):
    pass

kv = Builder.load_file("game.kv")

class MathApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MathApp().run()