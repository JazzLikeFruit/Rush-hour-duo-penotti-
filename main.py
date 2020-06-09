from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board(datafile)
    cardic = instance.load_cars(datafile)
    movements = 0
    records = []
    print(instance.load_board(empty_board))
    times=0
    while times < 15:

        # Kiest random car uit lijst met cars
        randomcar = random.choice(list(cardic))

        # Berekent de ruimte waarin car can bewegen
        ruimte = instance.check_space(randomcar)

        # Kiest een movement uit die reeks
        randommovement = random.choice(ruimte)

        # if instance.move("X", 1):
        #     empty_board = instance.create_board(datafile)
        #     instance.load_board(empty_board)

        # Check of movement valid is
        if instance.move(randomcar, randommovement):
            movements += 1
            randommovement
            # print('\n\nGELUKT!!\n\n')

            empty_board = instance.create_board(datafile)
          
            instance.load_board(empty_board)
            instance.save_board(movements)
            print(instance.save_board(movements))
            
            # if movements > 500 and instance.cars["X"].row != 5:
            #     movements = 0
            #     instance = board.Board(datafile)
            #     empty_board = instance.create_board(datafile)
            #     cardic = instance.load_cars(datafile)
            #     instance.load_board(empty_board)
            # 
            times+=1

        if instance.cars["X"].row == 5 or instance.move("X", 5-instance.cars["X"].row):
            times += 1

            empty_board = instance.create_board(datafile)
            print(instance.load_board(empty_board))
            instance.car_output()
            print()

            # records.append(movements)

            # Reload board
            # movements = 0
            # instance = board.Board(datafile)
            # empty_board = instance.create_board(datafile)
            # cardic = instance.load_cars(datafile)
            # instance.load_board(empty_board)
