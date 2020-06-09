from code.classes import cars, board
from numpy import random
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board(datafile)
    cardic = instance.load_cars(datafile)
    start = instance.load_board(empty_board)
    movements = 0
    times = 0
    records = []
    print(start)

    while times < 2:

        # Kiest random car uit lijst met cars
        randomcar = random.choice(list(cardic))

        # Berekent de ruimte waarin car can bewegen
        ruimte = instance.check_space(randomcar)

        # Kiest een movement uit die reeks
        randommovement = random.choice(ruimte)

        # Check als movement valid is
        if instance.move(randomcar, randommovement):

            movements += 1
            # print('\n\nGELUKT!!\n\n')

            empty_board = instance.create_board(datafile)
            # print(instance.load_board(empty_board))
            instance.load_board(empty_board)

            if instance.cars["X"].row == 5:
                times += 1
                print()
                print("Oplossingen:")
                print(instance.load_board(empty_board))
                # records.append(movements)
                print(movements)
                movements = 0

    # records.sort()

    # with open("results.csv", "a") as file:
    #     record = csv.writer(file, dialect="excel")
    #     record.writerow(records)

    # if instance.check_win() == True:
    #     print("win = true!")
    # else:
    #     print("win = false :(")

    # instance.car_output()
    # print("finit")
    # break

    # else:
    # print('\n\nerror!\n\n')
    # print(randomcar, cardic[randomcar].row, cardic[randomcar].col)
    # print('iteratie over')
