#Loads modules
import sys

import kivy
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


sys.path.append('/usr/lib/python3.4')

kivy.require('1.9.2') #uses current kivy version.





#TODO LOAD LIGHTSCREEN CLASS, INITIALIZE AND HAVE IT HAVE 2 BUTTONS, ON AND OFF.
#CONNECT WITH BLUETOOTH FOR A BUILD, THEN GIT PUSH.
class MainMenuScreen(Screen):
    def __init__(self, client, modules, **kwargs):
        super(MainMenuScreen,self).__init__(**kwargs)
        MainMenuScreen.client = client
        for module in modules:
            button = Button(text=module.moduleid, on_release=module.entered)
            self.ids.menulayout.add_widget(button)