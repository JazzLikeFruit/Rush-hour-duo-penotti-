from code.algorithms import random_algorithm, unique_moves, short_path, end_point
from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    cardic = instance.load_cars(datafile)
    #records = []
    instance.load_board(empty_board)
    print(instance.possible_movements())
    print(instance.load_board(empty_board))

    # --------------------------- Random reassignment --------------------------
    # movements = random_algorithm.randy(instance, cardic)
    # movements
    # --------------------------- Unique configuration each board --------------------------
    # movements_unique = unique_moves.unique(instance, cardic)
    # movements_unique
    # --------------------------- Unique configuration each board --------------------------
    # short_path = short_path.unique(instance, cardic)
    # short_path
    # --------------------------- End-point algorithm --------------------------
    # movements = end_point.End_point(instance, cardic)
    # movements.run()
    # --------------------------- Greedy algorithm --------------------------
