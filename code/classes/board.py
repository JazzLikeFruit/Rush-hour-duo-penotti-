import csv
import numpy as np
from .cars import Car


class Board():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)

    def load_cars(self, datafile):
        """
        Load the cars of a board
        """
        # Open datafile
        with open(datafile, 'r') as file:
            cars = {}
            reader = csv.DictReader(file)
            for row in reader:
                cars[row['car']] = Car(
                    row['orientation'], row['row'], row['col'], row['length'])  # Functie om het dummy bord op basis van de input van auto's te voorzien
        return cars

    def create_board(self, source_file):
        # definieer dimensie op basis van bestandsnaam
        self.dimension = int(source_file[-7])
        # Creeer een array met nullen op basis van dimensie om vol te zetten met auto's
        boarddummy = np.zeros((self.dimension+2, self.dimension+2), int).astype(str)

        for x in range(len(boarddummy[0])):
            boarddummy[x][0] = str(7-x)
            boarddummy[x][-1] = str(7-x)
        for x in range(len(boarddummy[0])):
            boarddummy[0][x] = '{}'.format(x)
            boarddummy[-1][x] = '{}'.format(x)
        boarddummy[0][0] = len(boarddummy)-1
        boarddummy[(len(boarddummy)-int(len(boarddummy)/2)-1)
                   ][-1] = '.'  # creer poortje aangegeven met '.'
        return boarddummy

    def load_board(self, empty_board):
        self.board = empty_board
        for key, row in self.cars.items():  # loop door input dataframe
            posx = 7-self.cars[key].col
            posy = self.cars[key].row

            self.board[posx][posy] = self.board[posx][posy].replace(
                '0', key)  # Vervang 0 met de relevante auto letter

            # check of de auto horizontaal of verticaal is georienteerd om te bepalen waar de volgende letter moet komen
            if self.cars[key].orientation == 'H':
                self.board[posx][posy +
                                 1] = self.board[posx][posy+1].replace('0', key)
                # check hoe groot de auto is om te bepalen of er nog een derde letter bij moet komen
                if self.cars[key].length == 3:
                    self.board[posx][posy +
                                     2] = self.board[posx][posy+2].replace('0', key)

            if self.cars[key].orientation == 'V':
                self.board[posx-1][posy] = self.board[posx -
                                                      1][posy].replace('0', key)
                if self.cars[key].length == 3:
                    self.board[posx-2][posy] = self.board[posx -
                                                          2][posy].replace('0', key)

        return self.board

    def move(self, car_key, blocks):

        # moves the car along the number of blocks depending on orientation
        if self.cars[car_key].orientation == "H":
            vast_y = 7 - self.cars[car_key].col
            eind_x = self.cars[car_key].row + blocks
            start_x = self.cars[car_key].row

            if blocks < 0:
                step = -1
                for x in range(start_x-1, eind_x-1, step):
                    print("startx:", start_x, "eind_x:",
                          eind_x, "vast_y:", vast_y, "x:", x)
                    print(self.board)
                    print("Onze coords; ", x, vast_y)
                    print("col:", self.cars["B"].col,
                          "row:", self.cars["B"].row)
                    print("Is dit gelijk aan 0?: ")
                    print(self.board[vast_y][x])
                    if self.board[vast_y][x] != "0":
                        return False
            else:
                step = 1
                for x in range(start_x+2, eind_x+1, step):
                    print("start_x:", start_x+1, "eind_x:",
                          eind_x, "vast_y:", vast_y, "x:", x)
                    print("Is dit gelijk aan 0?: ")
                    print(self.board[vast_y][x])
                    if self.board[vast_y][x] != "0":
                        return False

            self.cars[car_key].row = eind_x
            self.cars[car_key].move_count += 1
            self.cars[car_key].block_count += blocks
            return True

        elif self.cars[car_key].orientation == "V":
            vast_x = self.cars[car_key].row
            begin_y = 7-self.cars[car_key].col
            eind_y = 7-self.cars[car_key].col + blocks
            if blocks < 0:
                step = -1
                for y in range(begin_y+2, eind_y+2, step):
                    print(range(begin_y+2, eind_y+2, step))
                    print("begin_y:", begin_y, "eind_y:",
                          eind_y, "vast_x:", vast_x, "y:", y)
                    print("Is dit gelijk aan 0?: ")
                    print(self.board[y][vast_x])
                    if self.board[y][vast_x] != "0":
                        return False

            else:
                step = 1
                print(range(begin_y+2, eind_y+1, step))
                for y in range(begin_y+2, eind_y, step):
                    print("begin_y:", begin_y, "eind_y:",
                          eind_y, "vast_x:", vast_x, "y:", y)
                    print("Is dit gelijk aan 0?: ")
                    print(self.board[vast_x][y])
                    if self.board[y][vast_x] != "0":
                        return False
            self.cars[car_key].col = eind_y - 1
            print('Y-output:', 7 - eind_y)
            
            self.cars[car_key].move_count += 1
            self.cars[car_key].block_count += blocks
            return True

        return False

    def check_space(self, car_key):
        if self.cars[car_key].orientation == "H":
            front = 5-self.cars[car_key].row
            behind = -(self.cars[car_key].row) + 1
        elif self.cars[car_key].orientation == "V":
            front = 5-self.cars[car_key].col
            behind = -(self.cars[car_key].col) + 1
        output = [x for x in range(behind, front) if x != 0]

        return output

    def check_win(self):
        # checks if the game is finished by determining the winning position and the position of car X
        car_location = self.cars["X"].get_position()
        win_location = self.dimension - 1

        if car_location["col"] == win_location:
            return True
        else:
            return False

    def car_output(self):
        # generates informative output after a game is finished
        with open('output.csv', 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(["car", "move", "blocks"])

            for key in self.cars:
                #print(f"key = {key} moves: {self.cars[key].move_count} blocks: {self.cars[key].block_count}")
                car = key
                move = self.cars[key].move_count
                blocks = self.cars[key].block_count

                writer.writerow([car, move, blocks])
            

