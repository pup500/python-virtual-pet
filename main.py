import time
import threading
import sys

from inputter import Inputter
from messager import Messager
from pet.pet import Pet
from pet.food import Food, FoodItem

from colorama import init, Fore, Back, Style
init()  # Colorama init

class Main():
    '''Run the game. Facilitate interaction with pet.'''

    def __init__(self):
        self.running = True
        self.app_start_time = time.time()
        self.timer = threading.Timer(1.0, self.run)
        self.messager = Messager()
        self.inputter = Inputter()

    def begin(self):
        try:
            self.welcome()
            self.await_command()
        except KeyboardInterrupt:
            self.hide_activity()
            sys.exit(Fore.YELLOW + "\n Goodbye, thanks for playing!" + Style.RESET_ALL)

    def welcome(self):
        self.messager.print_garbage(20)
        self.messager.print_header(
            " Welcome to the Virtual Pet Creator!\n" +
            " (Press CTRL+C to exit)"
        )

    def run(self):
        if self.running:
            self.timer = threading.Timer(1.0, self.run)
            self.timer.start()
            self.print_pet_update()

    def hide_activity(self):
        self.running = False
        self.timer.cancel()

    def show_activity(self):
        self.running = True
        self.run()

    def await_menu(self):
        if input() == '':
            self.await_command()
        else:
            self.await_menu()

    def await_command(self):
        '''Accept user input.'''
        self.hide_activity()
        question = Back.BLACK + Fore.WHITE + '\n' + \
            'Enter a letter and press [ENTER]:' + Fore.GREEN + '\n' + \
            '    [C]reate pet \n' + \
            '    [W]alk pet \n' + \
            '    [F]eed pet \n' + \
            '    [P]lay with pet \n' + \
            '    [D]octor visit for your pet \n' + \
            '    [V]iew condition \n' + \
            '    [ENTER] let pet do what it wants \n' + Style.RESET_ALL + \
            'What will it be? '
        choice = input(question)
        if choice == "c":
            self.pet = Pet()
            self.pet.name = input('What do you want to name this pet? ')
            self.messager.print_subheader("Your pet, " + self.pet.name + " has been created!")
        elif choice == "w":
            self.pet.walk()
        elif choice == "f":
            amount = self.inputter.await_integer('How much food? ')
            self.pet.eat(amount)
        elif choice == "p":
            self.pet.play()
        elif choice == "d":
            self.pet.doctor()
        elif choice == "v":
            self.print_pet_state()
        elif choice == "": # ENTER was pressed.
            self.show_activity()
            self.await_menu()
            return
        else:
            print("Please use one of the available options...")
        self.await_command()

    def print_pet_state(self):
        self.messager.print_subheader(
            '====== ' + self.pet.name + ' ======' + '\n' + \
            'State: ' + str(self.pet.state) + '\n'
            'Age: ' + self.printable_pet_age + '\n' + \
            'Health: ' + str(self.pet.health) + '\n' + \
            'Calories: ' + str(self.pet.calories) + '\n' + \
            'Energy: ' + str(self.pet.energy) + '\n' + \
            'Happiness: ' + str(self.pet.happiness)
        )

    def print_pet_update(self):
        self.messager.print_random_colored(self.pet.name + " age: " + self.printable_pet_age)

    @property
    def printable_pet_age(self):
        seconds = self.pet.age

        seconds_in_day = 86400
        seconds_in_hour = 3600
        seconds_in_minute = 60

        days = seconds // seconds_in_day
        seconds = seconds - (days * seconds_in_day)

        hours = seconds // seconds_in_hour
        seconds = seconds - (hours * seconds_in_hour)

        minutes = seconds // seconds_in_minute
        seconds = seconds - (minutes * seconds_in_minute)

        return '%s days, %s hrs, %s mins, %s sec' % (days, hours, minutes, seconds)


m = Main()
m.begin()
