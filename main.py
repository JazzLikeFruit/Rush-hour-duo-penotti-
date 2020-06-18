from code.algorithms import random_algorithm, unique_moves, short_path, end_point, breadth_first
from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    cardic = instance.load_cars(datafile)
    records = []
    print("\nRUSH HOUR - Duo Penotti\n")
    print(instance.load_board(empty_board))
    print("\n====================================\n")
    print("Choose an alogithm to solve the puzzel with by typing the number :")
    algorithms = {'1': 'Random Algorithm', '2': 'Unique moves Algorithm',
                  '3': 'Optimalised moves Algorithm', '4': 'End Point Algorithm', '5': 'Sample of all algorithms', '6': 'Beadth first algorithm'}
    for algorithm in algorithms:
        print(f"- {algorithm} {algorithms[algorithm]}")

    while True:

        print("\nEnter your choice:")
        inputalgorithm = input().lower()
        if inputalgorithm not in algorithms:
            print('Incorrect algorithm select one of the following: ')

        else:
            print('Loading', algorithms[inputalgorithm], '...')
            break

    if inputalgorithm == '1':
        random_algorithm.randy(instance, cardic)
    elif inputalgorithm == '2':
        unique_moves.unique(instance, cardic)
    elif inputalgorithm == '3':
        short_path.unique(instance, cardic)
    elif inputalgorithm == '4':
        end_point.End_point(instance, cardic)
    elif inputalgorithm == '5':
        # optie om alle algoritmes x aantal keer te laten draaien en de data te verzmalen in een diagram / csv
        pass
    elif inputalgorithm == "6":
        run = breadth_first.Breathfirst(instance, cardic)
        run.run()
