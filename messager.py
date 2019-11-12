import random
from colorama import init, Fore, Back, Style
init()  # Colorama init


class Messager():
    '''Print colored output to screen.'''

    def __init__(self):
        '''init'''

    def print_header(self, message):
        print(
            Fore.MAGENTA + Back.BLACK + Style.BRIGHT + "\n"
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" +
            message + "\n" +
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
            Style.RESET_ALL + "\n"
        )

    def print_subheader(self, message):
        print(
            Fore.YELLOW + Back.BLACK + Style.BRIGHT + "\n"
            "————————————————————————————————————\n" +
            message + "\n" +
            "————————————————————————————————————" +
            Style.RESET_ALL + "\n"
        )

    def print_random_colored(self, message):
        '''Print message with randomized colors.'''
        print(self.random_colors + message + Style.RESET_ALL)

    @property
    def random_colors(self):
        fore = random.choice(Colors.FG)
        back = random.choice(Colors.BG)
        style = random.choice(Colors.STYLES)
        return fore + back + style

    def print_garbage(self, line_count):
        '''Having fun with color randomization.'''
        message = ""
        for line in range(line_count):
            message += self.random_colors + "ChAnGe ThE cOlOrS!!!!"
        print(message + Style.RESET_ALL)





class Colors():
    FG = [Fore.BLACK,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTWHITE_EX]
    BG = [Back.BLACK,
        Back.RED,
        Back.GREEN,
        Back.YELLOW,
        Back.BLUE,
        Back.MAGENTA,
        Back.CYAN,
        Back.WHITE,
        Back.LIGHTBLACK_EX,
        Back.LIGHTRED_EX,
        Back.LIGHTGREEN_EX,
        Back.LIGHTYELLOW_EX,
        Back.LIGHTBLUE_EX,
        Back.LIGHTMAGENTA_EX,
        Back.LIGHTCYAN_EX,
        Back.LIGHTWHITE_EX]
    STYLES = [Style.BRIGHT, Style.DIM, Style.NORMAL]
    RESETS = [Fore.RESET, Back.RESET, Style.RESET_ALL]


# class AnsiFore(AnsiCodes):
#     BLACK           = 30
#     RED             = 31
#     GREEN           = 32
#     YELLOW          = 33
#     BLUE            = 34
#     MAGENTA         = 35
#     CYAN            = 36
#     WHITE           = 37
#     RESET           = 39
#
#     # These are fairly well supported, but not part of the standard.
#     LIGHTBLACK_EX   = 90
#     LIGHTRED_EX     = 91
#     LIGHTGREEN_EX   = 92
#     LIGHTYELLOW_EX  = 93
#     LIGHTBLUE_EX    = 94
#     LIGHTMAGENTA_EX = 95
#     LIGHTCYAN_EX    = 96
#     LIGHTWHITE_EX   = 97
#
#
# class AnsiBack(AnsiCodes):
#     BLACK           = 40
#     RED             = 41
#     GREEN           = 42
#     YELLOW          = 43
#     BLUE            = 44
#     MAGENTA         = 45
#     CYAN            = 46
#     WHITE           = 47
#     RESET           = 49
#
#     # These are fairly well supported, but not part of the standard.
#     LIGHTBLACK_EX   = 100
#     LIGHTRED_EX     = 101
#     LIGHTGREEN_EX   = 102
#     LIGHTYELLOW_EX  = 103
#     LIGHTBLUE_EX    = 104
#     LIGHTMAGENTA_EX = 105
#     LIGHTCYAN_EX    = 106
#     LIGHTWHITE_EX   = 107
#
#
# class AnsiStyle(AnsiCodes):
#     BRIGHT    = 1
#     DIM       = 2
#     NORMAL    = 22
#     RESET_ALL = 0
#
# Fore   = AnsiFore()
# Back   = AnsiBack()
# Style  = AnsiStyle()
# Cursor = AnsiCursor()
