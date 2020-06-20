import copy
import time
import queue


class BreathFirst():
    """
    A Breath First algorithm that finds the solution with the least ammount of steps.
    """

    def __init__(self, instance):

        # Make Copy of instance
        self.instance_copy = instance

        self.queue = queue.Queue()

    # Load children of current state
    def build_children(self, instance, initial_movement):
        move_list = []

        # Add initial moves to new moves list
        for move in initial_movement:
            move_list.append(move)

        # Get possible movements for the current board
        posibilities = instance.possible_movements()

        # Add each possible movement to a different list with initial movement
        if posibilities:
            for movement in posibilities:

                # Copy list with initial movement
                list = copy.deepcopy(move_list)

                # Add one of the possible movements
                list.append(movement)

                # Add list to queue
                self.queue.put(list)

    # Runs the algorithm
    def run(self):

        # Get possible movements for first board
        first_momvements = self.instance_copy.possible_movements()

        # Add movement seperately to queue
        for movement in first_momvements:
            list = []
            list.append(movement)
            self.queue.put(
                list)

        while True:

            instance = copy.deepcopy(self.instance_copy)

            count = 0

            # get next movement from queue
            movement = self.queue.get()

            # Make movement using tuple
            for move in movement:

                # Plot tuple for move
                instance.move(move[-2], move[-1])

                # Reload board
                empty_board = instance.create_board()
                instance.load_board(empty_board)

                # Count movements
                count += abs(move[-1])

            # Check win
            if instance.check_win():
                empty_board = instance.create_board()
                return (count, instance.load_board(empty_board))

            else:
                # Get childeren of current board
                self.build_children(instance, movement)
