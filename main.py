import kivy 
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
import random 
import string

class MainWindow(Screen):
    pass


class SecondWindow(Screen):

    def updatePassword(self): 
        current = self.ids.currentPassword
        current.text = self.generatePassword()



    def generatePassword(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        All = lower + upper + num + symbols 
        # Store all possible strings in one large string 

        temp = random.sample(All, random.randint(8,16))
        password = "".join(temp)

        return password




class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()


