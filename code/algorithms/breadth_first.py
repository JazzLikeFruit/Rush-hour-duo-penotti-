import copy
import time
import datetime


class Breathfirst():
    """
    A Breath First algorithm that finds the solution with the least ammount of steps.
    """

    def __init__(self, instance, carslist):

        # Make Copy of instance
        self.instance_copy = instance
        self.cars = carslist

        self.queue = []

    # gets next state in queue

    def get_next_state(self):
        return self.queue.pop(0)

    # Load children of current state
    def build_children(self, instance, initial_movement):
        move_list = []

        # Add initial moves to new moves list
        for move in initial_movement:
            move_list.append(move)

        # Get possible movements for the current board
        posibilities = instance.possible_movements()

        # Add each possible movement to a different list with initial movement
        for movement in posibilities:

            # Copy list with initial movement
            list = copy.deepcopy(move_list)

            # Add one of the possible movements
            list.append(movement)

            # Add list to queue
            self.queue.append(list)

    # Runs the algorithm
    def run(self):

        # Count runtime
        begin_time = datetime.datetime.now()

        # Get possible movements for first board
        first_momvements = self.instance_copy.possible_movements()

        # Add movement seperately to queue
        for movement in first_momvements:
            list = []
            list.append(movement)
            self.queue.append(
                list)

        while True:

            instance = copy.deepcopy(self.instance_copy)
            count = 0

            # get next movement from queue
            movement = self.get_next_state()

            # Make movement
            for move in movement:
                instance.move(move[-2], move[-1])
                empty_board = instance.create_board()
                instance.load_board(empty_board)
                count += abs(move[-1])

            # Check win
            if instance.check_win():
                print(movement)
                return print(f'Solution found in {count} moves in {datetime.datetime.now() - begin_time}')

            else:
                # Get childeren of current board
                self.build_children(instance, movement)
