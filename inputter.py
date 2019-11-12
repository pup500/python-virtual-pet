
class Inputter():
    '''Accepts input and checks to make sure acceptable input is received.'''

    def __init__(self):
        pass

    def is_int(self, string):
        '''Return whether argument is an int'''
        try:
            int(string)
            # Exception will happen here on failure.
            return True
        except ValueError:
            return False

    def await_integer(self, message:str):
        '''Repeatedly ask for input if values entered aren't integers.'''
        string = input(message)
        if self.is_int(string):
            return int(string)
        else:
            print("Please enter an integer...")
            return self.await_integer(message)
