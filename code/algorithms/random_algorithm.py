from numpy import random
import csv
import random
import _pickle as cPickle
"""
Algorithm that randomly generates a solution. 
"""


def randy(inst, cars):

    movements = 0

    # Copy of the main game instance
    instance_copy = cPickle.loads(cPickle.dumps(inst, -1))

    # Run loop while game not winnable
    while not instance_copy.cars["X"].row == instance_copy.win_location:

        # Select random car
        randomcar = random.choice(list(cars))

        # Check movable spaces of the car
        movementspace = instance_copy.check_space(randomcar)

        # Choose a move randomly
        randommovement = random.choice(movementspace)

        if instance_copy.move(randomcar, randommovement):
            # Count movements made
            movements += 1

            # Reload board
            empty_board = instance_copy.create_board()
            result = instance_copy.load_board(empty_board)
        
    instance_copy.car_output()
    return (movements, result)
