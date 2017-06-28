from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

import kivy

from kivy.graphics.vertex_instructions import Rectangle

kivy.require('1.9.2')  # uses current kivy version.s


class ServerSelection(Screen):
    def __init__(self, **kwargs):
        super(ServerSelection, self).__init__(**kwargs)

    def addServer(self):
        popup = AddServerPopup()
        popup.open()


# Represents a server with:
# name,ip,status.
class Server(FloatLayout):
    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)


class AddServerPopup(Popup):

    def pingServer(self):
        print("Ping")
        pass

    def createServer(self):
        print("Pong")
        pass