#Loads modules
import sys

import kivy
from kivy.lang import Builder

from main.GUI.mainmenu.MainMenu import MainMenuScreen
from main.MQTTListener import MQTTManager
from main.modules.lights.light_widgets import LightSection, AddPopup
from main.modules.module import Module

sys.path.append('/usr/lib/python3.4')
Builder.load_file("modules/lights/light_screen.kv")

kivy.require('1.9.2') #uses current kivy version.

class LightScreen(Module):
    sections = [] #Fill with light sections.
    
    def __init__(self):
        super(LightScreen, self).__init__(name="lights", displayname="Lights")
    
    def add_popup(self):
        addpopup = AddPopup(self)
        addpopup.open()
    
    def add_section_popup(self, popup):
        popup.dismiss()
        name = popup.textinput.text
        device = popup.spinner.text
        argument = popup.argumentinput.text
        permission = 5
        MQTTManager.cm.varStore(self)
        MainMenuScreen.client.publish("server/modules/lights/create", name+","+device+","+str(permission)+","+str(argument))

    def add_section(self, name, permission, status):
        section = LightSection(section_name=name, status=status)
        print("Section created with name: "+name)
        self.sections.append(section)
        self.ids.scrollbody.add_widget(section)

    def add_section_payload(self, payload):
        info = payload.split(",")
        self.add_section(info[0],info[1], info[2])

    def on_enter(self, *args):
        self.sections.clear()
        self.ids.scrollbody.clear_widgets()
        MQTTManager.cm.varStore(self)
        MainMenuScreen.client.publish("server/modules/lights/retrieve", "")