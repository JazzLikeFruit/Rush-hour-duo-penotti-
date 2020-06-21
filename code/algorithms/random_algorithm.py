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

        # Check movable spaces of the car
        movement = instance_copy.possible_movements()

        # Choose a move randomly
        randommovement = random.choice(movement)

        # Perform movement if this is possible
        instance_copy.move(randommovement[-2], randommovement[-1])

        # Count movements made
        movements += 1

        # Reload board
        empty_board = instance_copy.create_board()
        result = instance_copy.load_board(empty_board)
    instance_copy.car_output()
    return (movements, result)
