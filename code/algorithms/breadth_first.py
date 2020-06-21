import copy
import time
import queue
import _pickle as cPickle


class BreathFirst():
    """
    A Breath First algorithm that finds the solution with the least ammount of steps.
    """

    def make_move(self, instance, car, movement):
        if instance.cars[car].orientation == 'H':
            instance.cars[car].row = instance.cars[car].row + movement

        if instance.cars[car].orientation == 'V':
            instance.cars[car].col = instance.cars[car].col - movement

    def __init__(self, instance):

        # Make Copy of instance
        self.instance_copy = instance

        # Define the queue
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
                list = cPickle.loads(cPickle.dumps(move_list, -1))

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

            move_count = 0

            # get next movement from queue
            movement = self.queue.get()

            # Make movement using tuple
            for move in movement:

                # Make movement
                self.make_move(instance, move[-2], move[-1])

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
