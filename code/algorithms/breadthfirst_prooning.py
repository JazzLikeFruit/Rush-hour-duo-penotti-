import time
import _pickle as cPickle
from .breadth_first import BreathFirst


class BreathFirst_P(BreathFirst):
    """
    Impliments the breadth first algorithm by not adding already seen boards to queue

    """
    # Make trie of seen boards

    def make_trie(self, root, dictionary):

        # Mark the end of board
        _end = '_end_'

        # root of trie
        current_dict = root

        # Loop through dictionary and add tuple to trie
        for key in dictionary:
            set1 = (key, dictionary[key])
            current_dict = current_dict.setdefault(
                set1, {})

        # Mark end of board
        current_dict[_end] = _end
        return root

    # Search for board in trie
    def in_trie(self, trie, dictionary):

        # Start of trie
        current_dict = trie

        # search trie for individual tuple
        for key in dictionary:
            set = (key, dictionary[key])

            # Return false if tuple not in trie
            if set not in current_dict:
                return False

            # Go to next tuple
            current_dict = current_dict[set]
        return True

    def run(self):

        # List of visited boards
        board_dict = dict()

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

        # Start with new board
        instance = self.instance_copy

        while True:

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
                if instance.cars[move[-2]].orientation == 'H':
                    instance.cars[move[-2]
                                  ].row = instance.cars[move[-2]].row + move[-1]
                else:
                    instance.cars[move[-2]
                                  ].col = instance.cars[move[-2]].col - move[-1]

                # Add movement made by the car to the move_count
                move_count += abs(move[-1])

            if self.in_trie(board_dict, car_dict):
                pass

            else:
                # Add car_dict to the list of already seen boards
                self.make_trie(board_dict, car_dict)

                empty_board = instance.create_board()
                instance.load_board(empty_board)

                # Check win
                if instance.check_win():

                    # Create a new board
                    empty_board = instance.create_board()
                    return(move_count, instance.load_board(empty_board))

                else:

                    # Get childeren of current board
                    self.build_children(instance, movement)

            # Return to initial board
            for move in movement:

                # Make movement
                if instance.cars[move[-2]].orientation == 'H':
                    instance.cars[move[-2]
                                  ].row = instance.cars[move[-2]].row - move[-1]
                else:
                    instance.cars[move[-2]
                                  ].col = instance.cars[move[-2]].col + move[-1]
