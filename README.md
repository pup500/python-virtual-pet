Virtual Pet
------------------------------------------------------------
Create a pet, feed it, play with it, take it to the doctor, just keep it alive!

This is a game of balancing where your virtual pet must be tended to in the proper amounts to prevent its death.

The pet should have variables to represent its condition.

    These variables get affected over the course of the pet's life.
    These variables collectively define the pet's state.

	When all health conditions are unmet, the pet will die.
	When all health conditions are met, the pet will live.
	When all health conditions are balanced, the pet will grow.

The pet should perform user-triggered functions.

    These functions change the pet's variables.
    These functions provide a message to be displayed during the function's operation.






Variables
---------------------------------------------------------------
(This is a rough outline of ideas for how to structure the virtual pet.)

- name
- birth_time
- @age (calculated from `birth_time`)
- calories
- energy
- happiness
- health: If this reaches 0, the pet dies.

- condition –– Something causes an effect over time, e.g., a virus.
- evolution –– growth stage


Methods
--------------------------------------------------------------
(This is a rough outline of ideas for how to structure the virtual pet.)

Each function will affect the pet's state in different ways.

# hatch –– Pet initialized. Starting conditions are displayed.
# die –– Pet destroyed. Ending conditions are displayed.

# USER-TRIGGERED COMMANDS

# eat
	# +happiness
	# +calories
# walk
	# +happiness
	# +health
	# -energy
# play
	# +happiness
	# -energy
# heal (from doctor visit)
	# +health
# react (Version 2)
	# to command (like a trick)

Autonomous Behaviors - Things pet will do on its own
----------------------------------------------------
# live
	# -calories
	# check all health conditions
# grow
	# increase capacity for health
# decay

# sleep
    Ver. 1: Run for 1 iteration. Will run again if energy is low.
	Ver. 2: Run for x iterations. Can be interrupted.
	# +health
	# +energy
# awake

# wander
    # randomly call `speak`
    # randomly call `hurt`
    # if energy is low, call `sleep`

# speak – Pet makes requests and describes its own condition.

# hurt – randomly called from `wander` to produce a temporary health event.
    # -happiness
	# from playing
	# from walking
	# from eating
	# from starving
	# from sadness



# If the pet gets too hungry, its happiness will decrease.
# If the pet gets very, very hungry, its health will decrease.
