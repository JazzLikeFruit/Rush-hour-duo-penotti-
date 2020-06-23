import copy
import time
import queue
import _pickle as cPickle


class BreathFirst():
    """
    A Breath First algorithm that finds the solution with the least amount of steps.
    """

    def make_move(self, instance, car, movement):
        if instance.cars[car].orientation == 'H':
            instance.cars[car].row = instance.cars[car].row + movement

        else:
            instance.cars[car].col = instance.cars[car].col - movement

    def __init__(self, instance):

        # Make Copy of instance
        self.instance_copy = instance

        # Define the queue
        self.queue = queue.Queue()

    # Load children of current state
    def build_children(self, instance, initial_movement):

        for movement in instance.possible_movements():

            # Copy list with initial movement
            movements = list(initial_movement)

            # Add one of the possible movements
            movements.append(movement)

            # Add list to queue
            self.queue.put(movements)

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

            instance = cPickle.loads(cPickle.dumps(self.instance_copy, -1))

            move_count = 0

            # get next movement from queue
            movement = self.queue.get()

            # Make movement using tuple
            for move in movement:

                # Make movement
                if instance.cars[move[-2]].orientation == 'H':
                    instance.cars[move[-2]
                                  ].row = instance.cars[move[-2]].row + move[-1]
                instance.cars[move[-2]
                              ].col = instance.cars[move[-2]].col - move[-1]

                # Add movement made by the car to the move_count
                move_count += abs(move[-1])

            # Load new board
            empty_board = instance.create_board()
            instance.load_board(empty_board)

            # Check win
            if instance.check_win():
                empty_board = instance.create_board()
                return (move_count, instance.load_board(empty_board))

            else:
                # Get childeren of current board
                self.build_children(instance, movement)
