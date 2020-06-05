from code.classes import cars, board

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    y = instance.create_board(datafile)
    print(instance.load_board(y))
