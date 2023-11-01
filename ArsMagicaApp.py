import ficha
import os
import random

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.image import AsyncImage


class CustomDropDown(DropDown):
    pass



class FichaScreen(Screen):
    #tipodropdown = ObjectProperty(None)
    tipoBotao = ObjectProperty(None)
    tipoLabel = ObjectProperty(None)


class ArsmagicaApp(App):
    def build(self):
        return sm

kv = Builder.load_file("ArsMagica.kv")
sm = ScreenManager()

screens = [FichaScreen(name="ficha")]

for Screen in screens:
    sm.add_widget(Screen)

sm.current = "ficha"

if __name__ == '__main__':
    ArsmagicaApp().run()

print(ficha.MagoIgnácio.FOR)