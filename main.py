<<<<<<< HEAD
from code.algorithms import random_algorithm, unique_moves, end_point
=======
from code.algorithms import random_algorithm, unique_moves, short_path
>>>>>>> ad7940f94037d9ac56dd8f4decd3e6fd345b10bd
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

    # --------------------------- Random reassignment --------------------------
    movements = random_algorithm.randy(instance, cardic)
    movements
    # --------------------------- Unique configuration each board --------------------------
<<<<<<< HEAD
    # movements_unique = unique_moves.unique(instance, cardic)
    # movements_unique
=======
    movements_unique = unique_moves.unique(instance, cardic)
    movements_unique
    # --------------------------- Unique configuration each board --------------------------
    short_path = short_path.unique(instance, cardic)
    short_path   
    # --------------------------- Greedy algorithm --------------------------
>>>>>>> ad7940f94037d9ac56dd8f4decd3e6fd345b10bd
