import os
from kivy.app import App
from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.properties import ObjectProperty
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
# from kivy.uix.image import AsyncImage

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'



class FichaScreen(Screen):

    # def calcula_custo_carac(self):
    #     # Int = self.retorna_inteiro(self.ids.Inteligencia.text)
    #     # Per = self.retorna_inteiro(self.ids.Percepção.text)
    #     # For = self.retorna_inteiro(self.ids.Força.text)
    #     # Vig = self.retorna_inteiro(self.ids.Vigor.text)
    #     # Pre = self.retorna_inteiro(self.ids.Presença.text)
    #     # Com = self.retorna_inteiro(self.ids.Comunicação.text)
    #     # Des = self.retorna_inteiro(self.ids.Destreza.text)
    #     # Rap = self.retorna_inteiro(self.ids.Rapidez.text)
    #     # custo_carac = self.calculaProgAri(Int) + self.calculaProgAri(Per) + self.calculaProgAri(For) + self.calculaProgAri(Vig) + self.calculaProgAri(Pre) + self.calculaProgAri(Com) + self.calculaProgAri(Des) + self.calculaProgAri(Rap)
    #     # ptDispon = 7 - custo_carac
    #     # self.ids.ptCarac.text = str(ptDispon)
    #
    # def calcula_custo_hab(self):
    #     # xp = (self.retorna_inteiro(self.ids.idade.text)-5)*15
    #     # hab1 = self.retorna_inteiro(self.ids.armas_de_uma_mao.text)
    #     # hab2 = self.retorna_inteiro(self.ids.armas_de_duas_maos.text)
    #     # custoHab = self.calculaProgAri(hab1)*5 + self.calculaProgAri(hab2)*5
    #     # xp = xp - custoHab
    #     # self.ids.xp.text = str(xp)

    def retorna_inteiro(self, strObj): # Pega o valor de uma label, string, e retorna um inteiro
        if strObj != '':
            return int(strObj)
        return 0

    def calculaProgAri(self, n): # faz o calculo da progressão aritmetica da soma de todos os números até n, é importante para o calculo do custo na compra de características
        if n >= 0:
            return n*(n+1)/2
        return n*(-n+1)/2

    def __init__(self, **kwargs):
        super(FichaScreen, self).__init__(**kwargs)
        #tipo_drop_down = TipoDropDown()
        #self.ids.tipo_botão.bind(on_release = tipo_drop_down.open)
        # self.ids.tipodropdown.dismiss() # fecha o tipo drop down, sem essa função o tipo dropdown aaparece aberto logo no início da aplicação
        # self.calcula_custo_carac() # preenche o n° de pontos disponíveis para caracteristicas, vai ser importante quando fichas buscar a ficha específica no banco de dados.

class TipoDropDown(DropDown):
    pass

kv = Builder.load_file("ArsMagica.kv")
sm = ScreenManager()

screens = [FichaScreen(name="ficha")]

for Screen in screens:
    sm.add_widget(Screen)

sm.current = "ficha"

class ArsmagicaApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    ArsmagicaApp().run()
