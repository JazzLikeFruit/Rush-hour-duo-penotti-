from numpy import random
import csv
import random
import copy
"""
Algorithm that forces unique configurations on every turn. 
"""


def unique(inst, cars):
    # Copy of the main game instance
    instance_copy = copy.deepcopy(inst)

    movements = 0

    def save_board(instance_copy):
        # saves car coordinates of current move in a dictionary
        key = movements
        step = {instance_copy.cars[car]: (
            instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        instance_copy.version[key] = step

        return instance_copy.version
    
    def empty_saves(instance_copy):
        instance_copy.version.clear()
        return instance_copy.version

    
    def check_move(instance_copy):
        # checks if move configuration has been achieved in earlier step and returns True if this is not the case and removes all keys after this point if it is the case
        current = {instance_copy.cars[car]: (instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        for board in instance_copy.version:
            if instance_copy.version[board] == current:
                for key in range(board, len(instance_copy.version)+1):
                    instance_copy.version.pop(key, None)
                return True

        return True    


    # Run loop while game not winnable
    while not instance_copy.check_win():
        dupe=instance_copy
        # Choose a car randomly
        randomcar = random.choice(list(cars))

        # Check movable spaces of the car
        movementspace = instance_copy.check_space(randomcar)

        # Choose a move randomly
        randommovement = random.choice(movementspace)

        # Perform movement if this is possible
        if dupe.move(randomcar, randommovement) and check_move(instance_copy):
            instance_copy.move(randomcar, randommovement)
            
            # Count movements made
            movements += 1

            # Reload board
            empty_board = instance_copy.create_board()
            print(instance_copy.load_board(empty_board))
            save_board(instance_copy)
    instance_copy.car_output()
    empty_saves(instance_copy)

    return print(f"Oplossing met geoptimaliseerd archief {movements} steps.")
    

