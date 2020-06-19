from numpy import random
import csv
import random
import copy
"""
Algorithm that randomly generates a solution. 
"""


def randy(inst, cars):

    movements = 0

    # Copy of the main game instance
    instance_copy = copy.deepcopy(inst)

    # Run loop while game not winnable
    while not instance_copy.cars["X"].row == instance_copy.win_location:

        # Choose a car randomly
        randomcar = random.choice(list(cars))

        # Check movable spaces of the car
        movementspace = instance_copy.check_space(randomcar)

        # Choose a move randomly
        randommovement = random.choice(movementspace)
        # if randomcar =='B':
        #     print(randomcar,movementspace, randommovement)
        # Perform movement if this is possible
        if instance_copy.move(randomcar, randommovement):
            # Count movements made
            movements += 1

            # Reload board
            empty_board = instance_copy.create_board()
            result=instance_copy.load_board(empty_board)
    instance_copy.car_output()
    empty_board = instance_copy.create_board()

    return (movements,result)
