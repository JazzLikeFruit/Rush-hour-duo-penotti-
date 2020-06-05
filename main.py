from code.classes import cars, board

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board(datafile)

    while True:
        print(instance.load_board(empty_board))

        car = input("which car? ")
        block = input("how many blocks? ")
        if instance.move(car, int(block)) == False:
            print("pech!!!!")

        empty_board = instance.create_board(datafile)

        print(instance.load_board(empty2_board))
