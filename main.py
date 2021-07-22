import kivy 
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.recycleview import RecycleView 

import random 
import string

saves = []

class Menu(Screen):
    pass


class passwordCreator(Screen):

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
    
    def getPassword(self): 
        print("test")
        return self.ids.currentPassword.text

    



class savingScreen(Screen):
    
    current_password = StringProperty('')
    
    def on_enter(self, *args):
        self.current_password = self.manager.get_screen('creatingPassword').ids.currentPassword.text
    
    def save(self):
        password = self.current_password
        description = self.ids.passwordDescription.text
        placeholder = "Password:  {password}    ||    Description: {description}".format(password = password, description = description)
        saves.append(placeholder)
    
    def get_data_index(self):
        return self.parent.get_view_index_at(self.center)
    
    def on_release(self):
        print(self.get_data_index())
    
        


class ExampleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(ExampleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in saves]
    
    def update_data(self):
        self.data = [{'text': str(x)} for x in saves]

class passwordList(Screen):
    pass


    
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()


