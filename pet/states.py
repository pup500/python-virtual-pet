from enum import Enum

from colorama import init, Fore, Back, Style
init() # Init Colorama


class StateType():
    def __init__(self, name, color):
        self.name = name
        self.color = color

class State():
    ALIVE = StateType('alive', Back.LIGHTGREEN_EX + Fore.WHITE)
    ASLEEP = StateType('asleep', Back.LIGHTBLACK_EX + Fore.BLUE)
    DEAD = StateType('dead', Back.RED + Fore.WHITE)

class Mood():
    NEUTRAL = StateType('neutral', Fore.WHITE)
    HAPPY   = StateType('happy', Fore.LIGHTYELLOW_EX)
    SAD     = StateType('sad', Fore.BLUE)
    ANGRY   = StateType('angry', Fore.RED)
    TIRED   = StateType('tired', Fore.LIGHTWHITE_EX)
    HUNGRY  = StateType('hungry', Fore.LIGHTRED_EX)
    BORED   = StateType('bored', Fore.GREEN)


# Enum syntax could be `class Mood(Enum)`
