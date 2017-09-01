#A module is treated exactly like a screen, but it also has other properties
#And methods that act as events or specific actions.


import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen

kivy.require('1.9.2') #uses current kivy version.

class Module(Screen):
    menu_screen = None #Main screen instance
    def __init__(self, **kwargs):
        super(Module, self).__init__(name=kwargs["name"])
        self.on_initialize()
        self.moduleid = kwargs["displayname"]
        App.get_running_app().sm.add_widget(self)
        print("Loaded module:", self.moduleid)

    def on_initialize(self):
        pass
    
    def entered(self, origin):
        App.get_running_app().sm.current = self.name
    
    
        