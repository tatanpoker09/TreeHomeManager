from kivy.uix.screenmanager import Screen
from main.MQTTListener import MQTTManager

class LoginScreen(Screen):
    def __init__(self, ip, port, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.ip = ip
        self.port = port

    def connect(self):
        username = self.ids["username"].text
        password = self.ids["password"].text
        print("Connecting to: ", self.ip, "with username: ", username, " and password ", password)
        m = MQTTManager(self.ip, self.port)
        m.setup()


