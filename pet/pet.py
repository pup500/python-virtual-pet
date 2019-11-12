import time
from pet.states import Mood, State
from pet.food import Food

class Pet():
    '''An animal to be cared for, fed, played with.'''

    def __init__(self):
        self.name = '(unnamed)'
        self.birth_time = time.time()
        self.health = 0 # Not enough = dead
        self.calories = 0 # Too many calories = sick
        self.energy = 0 # Too much energy = injury
        self.happiness = 0 # Not enough = sick
        self.mood = Mood.NEUTRAL
        self.state = State.ALIVE

    @property
    def age(self):
        '''Age in seconds.'''
        #timedelta(seconds=time.time() - pet.birth_time)
        return int(time.time() - self.birth_time)

    def play(self):
        print("Pet is eating.")

    def doctor(self):
        print("Pet is going to doctor.")

    def hurt(self):
        probability = .5
        is_hurt = random.random() < probability
        if is_hurt:
            print("Pet has sustained an injury!")

    def grow(self):
        print("Pet is growing.")

    def walk(self):
        print("Pet is walking.")

    # Advanced: [Food.CANDY, Food.CANDY]
    def eat(self, amount):
        for food in range(amount):
            print("Pet is eating piece", food, "from", amount, "pieces of food.")
            time.sleep(.2)

    def live(self):
        if self.calories == 0:
            self.emote(Mood.HAPPY)
        elif self.stomach > 100:
            self.emote(Mood.SAD)

    def emote(self, mood):
        print(mood.color + self.name + " is " + mood.name)

    def has_food(self):
        return len(self.food) > 0
