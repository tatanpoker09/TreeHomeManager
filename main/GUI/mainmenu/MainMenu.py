#Loads modules
import sys
import time

import kivy
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

sys.path.append('/usr/lib/python3.4')

kivy.require('1.9.2') #uses current kivy version.





#TODO LOAD LIGHTSCREEN CLASS, INITIALIZE AND HAVE IT HAVE 2 BUTTONS, ON AND OFF.
#CONNECT WITH BLUETOOTH FOR A BUILD, THEN GIT PUSH.
class MainMenuScreen(Screen):
    def __init__(self, client, modules, **kwargs):
        super(MainMenuScreen,self).__init__(**kwargs)
        MainMenuScreen.client = client
        Clock.schedule_interval(self.update_clock, 1)
        for module in modules:
            button = Button(text=module.moduleid, on_release=module.entered)
            self.ids.menulayout.add_widget(button)

    def update_clock(self, init):
        self.ids.clock.text = str(time.strftime('%d-%m-%Y     %H:%M:%S'))
