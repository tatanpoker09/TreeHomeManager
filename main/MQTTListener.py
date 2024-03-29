import paho.mqtt.client as mqtt
from kivy.app import App

from main.GUI import SpecialPopups
from main.GUI.loading.Initializer import LoadingScreen
from main.modules.CommandManager import CommandManager


class MQTTManager:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        MQTTManager.cm = CommandManager()

    def setup(self):
        mqttc = mqtt.Client()
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        try:
            mqttc.connect(self.ip, port=int(self.port), keepalive=60)
            mqttc.loop_start()
            App.get_running_app().sm.switch_to(LoadingScreen(name="loading", client=mqttc))
        except Exception as e:
            print(e)
            SpecialPopups.get_text_popup("Couldn't connect to the server!", 500, 500, "Server Connection Error", True).open()
            return

    def setup_bypass(self):
            App.get_running_app().sm.switch_to(LoadingScreen(name="loading", client=mqtt.Client()))

    def on_connect(self, client,  userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("main/tatanroom/lights")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload
        MQTTManager.cm.parse(topic=topic, payload=payload)