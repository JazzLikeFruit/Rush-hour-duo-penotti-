from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    cardic = instance.load_cars(datafile)
    movements = 0
    #records = []
    print(instance.load_board(empty_board))
    times = 0
    while times < 100:

        # Kiest random car uit lijst met cars
        randomcar = random.choice(list(cardic))

        # Berekent de ruimte waarin car can bewegen
        ruimte = instance.check_space(randomcar)

        # Kiest een movement uit die reeks
        randommovement = random.choice(ruimte)


        # Check of movement valid is
        if instance.move(randomcar, randommovement) and instance.check_move():
            movements += 1
            #print ('making move')
            empty_board = instance.create_board()
          
            instance.load_board(empty_board)
            instance.save_board(movements)

        if instance.check_win():
            times += 1
            print(movements)

            empty_board = instance.create_board()
            print(instance.load_board(empty_board))

            with open('with_check.csv', 'a', newline='') as output:
                writer = csv.writer(output)
                writer.writerow([times, movements])

            print()

            # records.append(movements)

            # Reload board
            movements = 0
            instance = board.Board(datafile)
            empty_board = instance.create_board()
            cardic = instance.load_cars(datafile)
            instance.load_board(empty_board)
