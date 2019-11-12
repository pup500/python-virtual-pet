from pet.pet import Pet
from pet.states import Mood, State
from pet.food import Food

class Duck(Pet):
	'''Classic Pythonic animal because all are objects duck-typed.'''

	def __init__(self):
		super().__init__()

	def walk(self):
		super().walk()
		print("Pet is also quacking.")

class Dog(Pet):
	'''A dog can do tricks!'''

	def __init__(self):
		super().__init__()
		self.tricks = []

	def learn_trick(self, trick):
		self.tricks.append(trick)
