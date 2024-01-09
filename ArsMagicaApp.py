import ficha
import os
import random

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import mysql.connector
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



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database = "banco"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM usuario")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

class FichaScreen(Screen):
    def calculaCustoCarac(self):
        Int = self.retornaInteiro(self.ids.Inteligencia.text)
        Per = self.retornaInteiro(self.ids.Percepção.text)
        For = self.retornaInteiro(self.ids.Força.text)
        Vig = self.retornaInteiro(self.ids.Vigor.text)
        Pre = self.retornaInteiro(self.ids.Presença.text)
        Com = self.retornaInteiro(self.ids.Comunicação.text)
        Des = self.retornaInteiro(self.ids.Destreza.text)
        Rap = self.retornaInteiro(self.ids.Rapidez.text)
        custoCarac = self.calculaProgAri(Int) + self.calculaProgAri(Per) + self.calculaProgAri(For) + self.calculaProgAri(Vig) + self.calculaProgAri(Pre) + self.calculaProgAri(Com) + self.calculaProgAri(Des) + self.calculaProgAri(Rap)
        ptDispon = 7 - custoCarac
        self.ids.ptCarac.text = str(ptDispon)

    def retornaInteiro(self, strObj): ##Pega o valor de uma label, string, e retorna um inteiro
        if strObj != '':
            return int(strObj)
        return 0

    def calculaProgAri(self, n): ##faz o calculo da progressão aritmetica da soma de todos os números até n, é importante para o calculo do custo na compra de características
        if n >= 0:
            return n*(n+1)/2
        return n*(-n+1)/2

    def salvarFicha(self):
        sql = ("insert into fichas (inteligência)"
               " value ")
        val = self.retornaInteiro(self.ids.Inteligencia.text)
        sql = sql + '(' + str(val) + ')'
        print(sql)
        mycursor.execute(sql)
        mydb.commit()

    def __init__(self, **kwargs):
        super(FichaScreen, self).__init__(**kwargs)
        self.ids.tipodropdown.dismiss() ##fecha o tipo drop down, sem essa função o tipo dropdown aaparece aberto logo no início da aplicação
        self.calculaCustoCarac() ##preenche o n° de pontos disponíveis para caracteristicas, vai ser importante quando fichas buscar a ficha específica no banco de dados.

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
