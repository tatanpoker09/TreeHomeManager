from kivy.app import App
from kivy.uix.screenmanager import Screen
import paho.mqtt.client as mqtt

from main.GUI.loading.Initializer import LoadingScreen


class LoginScreen(Screen):
    def __init__(self, ip, port, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.ip = ip
        self.port = port

    def connect(self):
        username = self.ids["username"].text
        password = self.ids["password"].text
        print("Connecting to: ", self.ip, "with username: ", username, " and password ", password)
        mqttc = mqtt.Client()
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        mqttc.username_pw_set(username, password)
        mqttc.connect(self.ip, 1883, 60)
        mqttc.loop_start()
        App.get_running_app().sm.switch_to(LoadingScreen(name="loading"))

    def on_connect(self, client,  userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    def on_message(self, client, userdata, msg):
        print("Message: "+msg.topic + " " + str(msg.payload))
