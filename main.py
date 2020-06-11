from code.classes import cars, board
import csv

if __name__ == '__main__':
    datafile = "data/Rushhour6x6_1.csv"
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    movements = 0
    records = []
    print(instance.load_board(empty_board))
    times=0
    algoritme= algoritme.random(datafile)
    file = input("save file name?\n")
    with open('{file}.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow("aantal stappen per oplossing")
    
    while times < 1:
        car=algoritme[0]
        movement=algoritme[1]
        

        # Check of movement valid is
        if instance.move(car, movement) and instance.check_move():
            movements += 1

            empty_board = instance.create_board()
            
            instance.load_board(empty_board)
            instance.save_board(movements)

        if instance.check_win():
            times += 1

            empty_board = instance.create_board()
            print(instance.load_board(empty_board))
            instance.car_output()
            print(f"finished in {movements} steps")

            with open('{file}.csv', 'w', newline='') as output:
                writer.writerow(movements)
            # records.append(movements)

            # Reload board
            # movements = 0
            # instance = board.Board(datafile)
            # empty_board = instance.create_board(datafile)
            # cardic = instance.load_cars(datafile)
            # instance.load_board(empty_board)
