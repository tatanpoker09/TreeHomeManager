from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from main.GUI.ServerSelection import ServerSelection

Builder.load_file("GUI/serverselection.kv")
Builder.load_file("GUI/loginscreen/loginscreen.kv")
Builder.load_file("GUI/mainmenu/menu_screen.kv")
Builder.load_file("GUI/loading/loading_screen.kv")


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