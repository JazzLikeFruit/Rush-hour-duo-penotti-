from code.algorithms import random_algorithm
from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    cardic = instance.load_cars(datafile)
    #records = []
    print(instance.load_board(empty_board))

    # --------------------------- Random reassignment --------------------------
    movements = random_algorithm.randy(instance, cardic)
    print(movements)

    # --------------------------- Random reassignment --------------------------
