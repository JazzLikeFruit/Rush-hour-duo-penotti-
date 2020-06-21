import copy
import time
import _pickle as cPickle
from .breadth_first import BreathFirst


class BreathFirst_P(BreathFirst):
    """
    Impliments the breadth first algorithm by not adding already seen boards to queue

    """

    def run(self):
        start_time = time.time()

        # List of visited boards
        board_list = []

        # Representation of a board by recording the movement made by each car
        car_dict = {}

        # Get possible movements for first board
        first_momvements = self.instance_copy.possible_movements()

        # Add  initial movement seperately to queue
        for movement in first_momvements:
            list = []
            list.append(movement)
            self.queue.put(
                list)

        while True:

            # Start with new board
            instance = cPickle.loads(cPickle.dumps(self.instance_copy, -1))

            # Keep count of each movement made by car
            move_count = 0

            # Create new cardict
            for car in instance.cars:
                car_dict[car] = 0

            # get next movement from queue
            movement = self.queue.get()

            # Make movement
            for move in movement:

                # Add movement to car in cardict
                car_dict[move[-2]] = car_dict[move[-2]] + move[-1]

                # Make movement
                self.make_move(instance, move[-2], move[-1])

                # Add movement made by the car to the move_count
                move_count += abs(move[-1])

            if car_dict in board_list:

                # Go to next iteration without adding movement to queue
                continue

            else:

                # Add car_dict to the list of already seen boards
                board_list.append(dict(car_dict))

                # Load new board
                empty_board = instance.create_board()
                instance.load_board(empty_board)

                # Check win
                if instance.check_win():

                    # Create a new board
                    print("--- %s seconds ---" % (time.time() - start_time))

                    empty_board = instance.create_board()
                    return(move_count, instance.load_board(empty_board))

                else:

                    # Get childeren of current board
                    self.build_children(instance, movement)
