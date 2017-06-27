from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from GUI.ServerSelection import ServerSelection

Builder.load_file("GUI/serverselection.kv")


class TreeApp(App):
    def __init__(self, **kwargs):
        super(TreeApp, self).__init__(**kwargs)
        self.sm = ScreenManager()

    def build(self):
        self.sm.switch_to(ServerSelection(name="serverselect"))
        return self.sm


if __name__ == '__main__':
    app = TreeApp()
    app.run()
