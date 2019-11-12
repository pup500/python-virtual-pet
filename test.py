import time

class Test():
    running = True

    def __init__(self):
        # We can calculate how much time has passed in order to update our pet's attributes.
        # All we need to do is call the update function and calculate time passed.
        # We can multiply that value by the function amount modifiers to create a delta.
        # We can apply that delta to all modified attributes.
        # The only problem may be interrupting the sleeping with user input.
        self.sleep()

    def decide(self):
        while Test.running:
            print("decide", Test.running)
            choice = input('Press [ENTER] to exit, "e" to sleep')
            if choice == "":
                print("[ENTER] received, exiting")
                Test.running = False
                exit()
            if choice == "e":
                print("e received, so running sleep")
                Test.running = True
                self.sleep()

    def sleep(self):
        try:
            while Test.running:
                print('sleeping')
                time.sleep(1.3)
                print('After: %s\n' % time.ctime())
        except KeyboardInterrupt as k:
            print('\n\nKeyboard exception received: ', k.args)
            self.decide()

t = Test()
