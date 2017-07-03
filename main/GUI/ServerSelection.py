from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from main.GUI.ServerListener import ThreadedClient
import kivy

kivy.require('1.9.2')  # uses current kivy version.s


class ServerSelection(Screen):
    servers = []

    def __init__(self, **kwargs):
        super(ServerSelection, self).__init__(**kwargs)

    def create_server(self):
        popup = AddServerPopup()
        #Can't instantiate this variable in an init. Apparently it crashes. Only the greek gods may know why.
        popup.set_server_selection(self)
        popup.open()

    def add_server(self, server):
        self.servers.append(server)
        self.ids.scrollbody.add_widget(server)

    def delete_server(self, server):
        self.servers.remove(server)
        self.ids.scrollbody.remove_widget(server)


# Represents a server with:
# name,ip,status.
class Server(FloatLayout):
    def __init__(self, servers,**kwargs):
        super(Server, self).__init__()
        try:
            self.name = kwargs["name"]
            self.ip = kwargs["ip"]
        except KeyError:
            pass
        self.status = "Disconnected" # disconnected, the server must be pinged to retrieve the value.

        self.size_hint = (0.4,None)
        self.size = (500, 100)

        self.connect_button = Button(size_hint= (0.1,1), pos_hint = {"x": 0, 'y':0}, text="Connect", on_press=lambda connect: self.connect())
        self.add_widget(self.connect_button)

        self.name_label = Label(size_hint = (0.3, 1.0), pos_hint = {"x": 0.2, 'y':0.3}, font_size=30, halign="left", valign="middle", text=self.name)
        self.add_widget(self.name_label)

        self.ip_label = Label(size_hint = (0.3, 1.0), pos_hint = {"x": 0.15, 'y':0}, font_size=30, halign="left", valign="middle", text=self.ip)
        self.add_widget(self.ip_label)

        self.edit_button = Button(size_hint= (0.08,0.8), pos_hint = {"x": 0.8, 'y':0.1}, text="Edit", font_size=30)
        self.add_widget(self.edit_button)

        self.delete_button = Button(size_hint= (0.08,0.8), pos_hint = {"x": 0.9, 'y':0.1}, text="Delete", font_size=30, on_press=lambda delete: servers.delete_server(self))
        self.add_widget(self.delete_button)

        self.name_label.bind(size=self.name_label.setter("text_size"))

    def connect(self):
        port = 7727
        client = ThreadedClient(self.ip, port)
        client.start()

class AddServerPopup(Popup):
    #cause fuck logic right?
    def set_server_selection(self, servers):
        self.sselection = servers

    def ping_server(self):
        print("Ping")

    def create_server(self):
        name = self.ids.servername.text
        ip = self.ids.serverip.text
        server = Server(self.sselection, name=name, ip=ip)
        ServerSelection.add_server(self.sselection, server)
        self.dismiss()
        print("Server: "+name+" with ip: "+ip+" created")