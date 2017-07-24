#Loads modules
import asyncio  # Multithreading
import inspect
import os  # we need it to load modules
from pydoc import locate
import sys
import importlib

import kivy
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, FadeTransition, Screen

from main.GUI.mainmenu.MainMenu import MainMenuScreen
from main.modules.module import Module

sys.path.append('/usr/lib/python3.4')



kivy.require('1.9.2') #uses current kivy version.



#Loading Screen:
#   Shows a splash screen while (TODO) Async configuration is loading
#   in the background

modules = [] #Holds all module names. No need for a whole module storage.
class LoadingScreen(Screen):
    #Constructor to keep the screenmanager object
    def __init__(self, client, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        self.client = client

    #Triggers when this Screen is entered.
    def on_enter(self):
        self.load_modules()
        self.setup()
        
        treeLabel = Label(text="Tree", opacity=0, center_y=10, font_size = "180sp")
        self.add_widget(treeLabel)
        anim = Animation(opacity = 1, duration = 2)
        anim.bind(on_complete=lambda x,y : self.labelAnimFinished(treeLabel))
        anim.start(treeLabel)

    #Called after 'Tree' label opacity is changed to 1. (after 4 seconds)
    def labelAnimFinished(self, widget):
        Clock.schedule_once(self.screen_callback, 2)

    #After another 4 seconds this is called to jump into the menu screen.
    def screen_callback(self, dt):
        menu = MainMenuScreen(client=self.client, modules=modules, name="menu")
        Module.menu_screen = menu
        App.get_running_app().sm.switch_to(menu, transition=FadeTransition())
    
    
    #Loads all modules 
    def load_modules(self):
        for f in os.listdir("modules"):
            f = os.path.join("modules", f)
            if os.path.isdir(f):
                moduledir = self.get_module(f)
                if moduledir!=None:
                    moduledir = moduledir.replace(".py", "").replace("\\", ".").replace("/",".")
                    module = importlib.import_module(moduledir)
                    clsmembers = inspect.getmembers(module, inspect.isclass)
                    for member in clsmembers:
                        if(member[1].__module__==moduledir):
                            instance = locate(moduledir+"."+member[0])
                            module = instance() 
                            modules.append(module)
                            break
                    
    #returns None if it isn't a module.
    def get_module(self, directory):
        module = None
        for d in os.listdir(directory):
            count = d.split(".")
            try:
                if count[1]=="py":
                    module = os.path.join(directory, d)
                    break
            except IndexError:
                pass
        return module


    def setup(self):
        self.client.subscribe("manager/bluetooth/devices")