import random

from kivy.lang import Builder

from main.GUI import SpecialPopups
from main.modules.module import Module

Builder.load_file("modules/randomnumber/randomnumber.kv")


class RandomNumber(Module):
    def __init__(self):
        super(RandomNumber, self).__init__(name="number", displayname="Random Number")

    def generate_random(self):
        try:
            numberfrom = int(self.ids.numberfrom.text)
            numberto = int(self.ids.numberto.text)
            self.ids.number.text = str(random.randint(numberfrom, numberto))
        except ValueError:
            SpecialPopups.get_text_popup("Wrong format!\nMake sure to input the lowest number on the left\nthe biggest one on the right\n and don't input any non-digit characters", 500, 500, "Bad Format Error", True).open()
