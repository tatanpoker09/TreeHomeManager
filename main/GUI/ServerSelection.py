from kivy.input.providers.mouse import Color
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

import kivy
from kivy.uix.widget import Widget

from kivy.graphics.vertex_instructions import Rectangle

kivy.require('1.9.2')  # uses current kivy version.s


class ServerSelection(Screen):
    def __init__(self, **kwargs):
        super(ServerSelection, self).__init__(**kwargs)


# Represents a server with:
# name,ip,status.
class Server(Widget):

    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)
        if(kwargs.has_key("name")):
            self.name = kwargs["name"]
