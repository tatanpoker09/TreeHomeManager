from main.modules.lights.light_widgets import AddPopup


class CommandManager:
    def varStore(self, var):
        self.store = var

    def __init__(self):
        pass

    def parse(self, topic, payload):
        print(topic, payload)
        if(topic=="manager/bluetooth/devices"):
            AddPopup.devices.append(str(payload.decode()))
            self.store.update()
        elif(topic=="manager/bluetooth/devices"):
            AddPopup.devices.append(str(payload.decode()))
            self.store.update()