#Loads modules
import sys

import kivy
from kivy.app import App
from kivy.lang import Builder

from main.modules.module import Module

sys.path.append('/usr/lib/python3.4')
Builder.load_file("modules/cameras/cameras.kv")


kivy.require('1.9.2') #uses current kivy version.



class CameraScreen(Module):
    def __init__(self):
        #TODO OPEN SERIAL COMMUNICATION
        super(CameraScreen, self).__init__(name="cam", displayname="Cameras")

    def back(self):
        App.get_running_app().sm.current = "menu"
        
