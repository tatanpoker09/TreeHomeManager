import time

from kivy.clock import Clock
from kivy.core.text import Label


class ClockWidget(Label):
    def __init__(self, inittime):
        Clock.schedule_interval(self.update, 1)

    def update(self):
        self.text = str(time.strftime('%d-%m-%Y  %H:%M:%S'))