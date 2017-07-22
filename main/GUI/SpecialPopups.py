from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

def get_text_popup(text, size_x, size_y):
    content = FloatLayout()
    content.add_widget(Label(text=text, pos_hint={'x': 0.2, 'y':0.2}))
    p = Popup(content=content, size_hint=(None, None), size=(size_x, size_y))
    return p