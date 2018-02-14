'''
Created on Feb 11, 2017

@author: Tatan
'''
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from main.GUI.mainmenu.MainMenu import MainMenuScreen
from main.GUI.widgets.ButtonImage import ButtonImage


class LightButton(ButtonBehavior, Image):
    pass
        
class LightSection(FloatLayout):
    def __init__(self, **kwargs):
        super(LightSection, self).__init__()
        try:
            self.section_name = kwargs["section_name"]
            self.status =  kwargs["status"]
        except KeyError:
            pass
        
        self.size_hint = (0.8,None)
        self.size = (1000, 70)
        self.status_button = ButtonImage(size_hint= (0.1,1), pos_hint = {"x": 0, 'y':0}, on_press=self.change_status, source="../resources/Lights"+self.status+".png")
        self.name_label = Label(size_hint = (0.5, 1.0), pos_hint = {"x": 0.1, 'y':0}, font_size=30, halign="left", valign="middle")
        self.status_label = Label(size_hint = (0.3, 1.0), pos_hint = {"x": 0.6, 'y':0}, text=self.status, font_size=30, text_size = self.size, halign="left", valign="middle")
        self.config_button = Button(size_hint= (0.1,1), pos_hint = {"x": 0.9, 'y':0}, text="Config", font_size=30, on_press=self.config)
        self.name_label.bind(size=self.name_label.setter("text_size"))
        self.add_widget(self.status_label)
        self.add_widget(self.status_button)
        self.add_widget(self.name_label)
        self.add_widget(self.config_button)
        self.status_label.text = self.status
        self.status_button.source = "../resources/Lights"+self.status+".png"
        Clock.schedule_once(self.callback)
    
    def callback(self, dt):
        self.name_label.text = self.section_name
    
    def change_status(self, origin):
        if self.status!="Disconnected":
            if self.status=="Off":
                self.status="On"
                MainMenuScreen.client.publish("server/modules/lights/"+self.section_name, True)
            else:
                self.status="Off"
                MainMenuScreen.client.publish("server/modules/lights/"+self.section_name, False)
            self.status_label.text = self.status
            self.status_button.source = "../resources/Lights"+self.status+".png"
        else:
            self.status = "Off"
            self.change_status(None)
            self.status_button.source = "../resources/Lights"+self.status+".png"

            
    def config(self, origin):
        pass
    
class AddPopup(Popup):
    devices = []
    def __init__(self, section):
        content = FloatLayout()
        self.spinner = Spinner(text="Devices: ", values=AddPopup.devices, pos_hint = {"x": 0, 'y':0.6}, size_hint = (0.2,0.2), text_autoupdate=True)
        content.add_widget(self.spinner)
        self.retrieve_button = Button(text="Retrieve Devices", pos_hint = {"x": 0.6, 'y':0.6}, size_hint = (0.2,0.2), on_press=lambda search: self.retrieve_devices())
        content.add_widget(self.retrieve_button)
        self.search_button = Button(text="Search Devices", pos_hint = {"x": 0.3, 'y':0.6}, size_hint = (0.2,0.2), on_press=lambda search: self.search_devices())
        content.add_widget(self.search_button)
        self.textinput = TextInput(text="Name", multiline=False, pos_hint = {"x": 0, 'y':0.5}, size_hint=(0.8, 0.1))
        content.add_widget(self.textinput)
        self.argumentinput = TextInput(text="Argument", multiline=False, pos_hint = {"x": 0, 'y':0.3}, size_hint=(0.3, 0.1))
        content.add_widget(self.argumentinput)
        self.closebutton = Button(text="Save",  pos_hint = {"x": 0, 'y':0.1}, size_hint=(0.8, 0.1), on_press=lambda popup: section.add_section_popup(self))
        content.add_widget(self.closebutton)
        self.update()
        super(AddPopup, self).__init__(title="Add LightSection", content=content,size_hint=(0.5,0.5), auto_dismiss=True)

    def search_devices(self):
        devices = []
        from main.MQTTListener import MQTTManager
        MQTTManager.cm.varStore(self)
        MainMenuScreen.client.publish("server/peripheral/bluetooth/search", "")

    def retrieve_devices(self):
        devices = []
        from main.MQTTListener import MQTTManager
        MQTTManager.cm.varStore(self)
        MainMenuScreen.client.publish("server/peripheral/bluetooth/retrieve", "")



    def update(self):
        self.spinner.values = AddPopup.devices