from enum import Enum

from colorama import init, Fore, Back, Style
init() # Init Colorama


class FoodItem():
	def __init__(self, name="?", health=0, dizzy=0, sick=0):
		self.name = name
		self.health = health
		self.dizzy = dizzy
		self.sick = sick
		self.calories = 0

class Food(Enum):
	CANDY = FoodItem("candy", 3, 1, 0)
	CANDY.calories = 100


# 🍇☕️🍵🍰🍓🍏🍊🥥🍌🍔🍟🥗🍡🍕🌮🌭🥑🍦🍭🍺🍷🥃🍸🍹🍫🥐🥦🍒🥕
