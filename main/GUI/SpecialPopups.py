from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup


def get_text_popup(text, size_x, size_y, title, close):
    content = FloatLayout()
    content.add_widget(Label(text=text, pos_hint={'x': 0.1, 'y':0.2}))
    p = Popup(size_hint=(None, None), size=(size_x, size_y), title= title)
    if close:
        closebutton = Button(text="close", size_hint=(0.2, 0.15), pos_hint={"x": 0.8, "y":0.2}, on_release=p.dismiss)
        content.add_widget(closebutton)

    p.content = content
    return p