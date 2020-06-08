from code.classes import cars, board
from numpy import random

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board(datafile)
    cardic = instance.load_cars(datafile)
    start = instance.load_board(empty_board)
    print(start)
    while True:

        #car = input("which car? ").upper()
        #block = input("how many blocks? ")

        # randomcar = random.choice(list(cardic))
        # print('Auto: ', randomcar, 'POS: ',
        #        "row", cardic[randomcar].row, "col", cardic[randomcar].col)
        # ruimte = instance.check_space(randomcar)
        # print ('Ruimte: ', ruimte)
        # randommovement = random.choice(ruimte)
        # print ('Verplaatsing: ', randommovement)

        if instance.move("C", -1) == True:
            print('\n\nGELUKT!!\n\n')
            #print('OUDE COORDS:', cardic[randomcar].col, cardic[randomcar].row)
            # if cardic[randomcar].orientation == 'H':
            #    cardic[randomcar].row += randommovement
            # elif cardic[randomcar].orientation == 'V':
            #    cardic[randomcar].col += randommovement
            # #print('NIEUWE COORDS: ',
            #       cardic[randomcar].col, cardic[randomcar].row)
            empty_board = instance.create_board(datafile)
            print(instance.load_board(empty_board))
            # print(randomcar, cardic[randomcar].col, cardic[randomcar].row)
            
        else:
            print('\n\nerror!\n\n')
            # print(randomcar, cardic[randomcar].row, 7-cardic[randomcar].col)
        print('iteratie over')
        break

        # print(instance.load_board(empty2_board))
