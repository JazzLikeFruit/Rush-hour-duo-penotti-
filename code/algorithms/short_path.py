import random
import copy
import _pickle as cPickle
"""
Algorithm that optimizes total movements based on saved versions of previous boards. 
"""


def short(inst, cars):
    # Copy of the main game instance
    instance_copy = cPickle.loads(cPickle.dumps(inst, -1))

    movements = 0

    def save_board(instance_copy):
        # Saves car coordinates of current move in a dictionary
        key = movements
        step = {instance_copy.cars[car]: (
            instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        instance_copy.version[key] = step

        return instance_copy.version
    
    def empty_saves(instance_copy):
        # Clear the dictionary
        instance_copy.version.clear()
        return instance_copy.version

    
    def check_move(instance_copy):
        # Checks if move configuration has been achieved in earlier step and returns True if this is not the case and removes all keys after this point if it is the case
        current = {instance_copy.cars[car]: (instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        for board in instance_copy.version:
            if instance_copy.version[board] == current:
                for key in range(board, len(instance_copy.version)+1):
                    instance_copy.version.pop(key, None)
                return (True, len(instance_copy.version))

        return [False] 


    # Run loop while game not winnable
    while not instance_copy.cars["X"].row == instance_copy.win_location:

        randomcar = random.choice(list(cars))

        # Check movable spaces of the car
        movementspace = instance_copy.check_space(randomcar)

        # Choose a move randomly
        randommovement = random.choice(movementspace)
        
        if instance_copy.move(randomcar, randommovement):

            # Check if move leads to a configuration that has been seen before
            check=check_move(instance_copy)

            # If true reset the total movements
            if check[0]:
                movements = check[1]
            # Else add 1 to movements
            else:
                movements += 1
        
        # Reload board & save board
        save_board(instance_copy)
        empty_board = instance_copy.create_board()
        result=instance_copy.load_board(empty_board)
    
    instance_copy.car_output()
    empty_saves(instance_copy)
    return (movements, result)
    

