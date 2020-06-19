import csv
import numpy as np
from .cars import Car
import re


class Board():
    """
    Creates a board filled with cars and other functionalities to implement the game Rush Hour
    """

    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)
        self.version = {}

        # define dimension based on name source file
        self.dimension = int(re.search(r"\d+", source_file)[0])

        self.win_location = self.dimension - 1

    def load_cars(self, datafile):
        # load cars dictionary from datafile input
        number = int(re.search(r"\d+", datafile)[0]) + 1

        with open(datafile, 'r') as file:
            cars = {}
            reader = csv.DictReader(file)

            # loop through input file to add cars to dictionary
            for row in reader:
                cars[row['car']] = Car(
                    row['orientation'], row['row'],  (number - int(row['col'])), row['length'])  # Functie om het dummy bord op basis van de input van auto's te voorzien
        return cars

    def create_board(self):
        # creates board as an array filled with 0s based on dimension
        boarddummy = np.zeros(
            (self.dimension + 2, self.dimension + 2), int).astype(str)

        # for x in range(len(boarddummy[0])):
        #     boarddummy[x][0] = str(x)
        #     boarddummy[x][-1] = str(x)

        # for y in range(len(boarddummy[0])):  
        #     boarddummy[0][y] = '{}'.format(y)
        #     boarddummy[-1][y] = '{}'.format(y)


        for x in range(len(boarddummy[0])):
            boarddummy[x][0] = '|'
            boarddummy[x][-1] = '|'
            boarddummy[0][x] = '|'
            boarddummy[-1][x] = '|'
        boarddummy[(len(boarddummy) - int(len(boarddummy) / 2) - 1)
                   ][-1] = '.'  # creates board exit with '.'
        return boarddummy

    def load_board(self, empty_board):
        self.board = empty_board

        # loop through cars dictionary to fill board
        for key, row in self.cars.items():
            posx = self.cars[key].col
            posy = self.cars[key].row

            # replace 0s on board with car name chars
            self.board[posx][posy] = self.board[posx][posy].replace(
                '0', key)

            # determine car orientation to place car correctly on the board
            if self.cars[key].orientation == 'H':
                self.board[posx][posy +
                                 1] = self.board[posx][posy + 1].replace('0', key)

                # determine car size and add a block if the car length = 3
                if self.cars[key].length == 3:
                    self.board[posx][posy +
                                     2] = self.board[posx][posy + 2].replace('0', key)

            if self.cars[key].orientation == 'V':
                self.board[posx-1][posy] = self.board[posx -
                                                      1][posy].replace('0', key)
                if self.cars[key].length == 3:
                    self.board[posx-2][posy] = self.board[posx -
                                                          2][posy].replace('0', key)

        return self.board

    def check_move(self, car_key, blocks):
        step = 1

        # moves the car along the number of blocks depending on orientation
        if self.cars[car_key].orientation == "H":
            const_y = self.cars[car_key].col
            end_x = self.cars[car_key].row + blocks
            start_x = self.cars[car_key].row

            # determine if the car moves in positive or negative direction
            if blocks < 0:

                for x in range(start_x - 1, end_x - 1, -step):
                    if self.board[const_y][x] != "0":
                        return False
            else:

                start = start_x + self.cars[car_key].length
                end = end_x + self.cars[car_key].length

                for x in range(start, end, step):
                    if self.board[const_y][x] != "0":
                        return False
            return True

        elif self.cars[car_key].orientation == "V":
            const_x = self.cars[car_key].row
            start_y = self.cars[car_key].col
            end_y = self.cars[car_key].col - blocks

            if blocks < 0:
                end_y = self.cars[car_key].col + -(blocks)
                start = start_y
                end = end_y

                if self.cars[car_key].length == 3:
                    start += 1
                    end += 1

                for y in range(start + 1, end + 1, step):
                    if self.board[y][const_x] != "0":
                        return False

            else:
                for y in range(start_y - 2, end_y - 2, -step):
                    if self.board[y][const_x] != "0":
                        return False
            return True
        return False

    def move(self, car_key, blocks):
        step = 1

        # moves the car along the number of blocks depending on orientation
        if self.cars[car_key].orientation == "H":
            const_y = self.cars[car_key].col
            end_x = self.cars[car_key].row + blocks
            start_x = self.cars[car_key].row

            # determine if the car moves in positive or negative direction
            if blocks < 0:

                for x in range(start_x - 1, end_x - 1, -step):
                    if self.board[const_y][x] != "0":
                        return False
            else:

                start = start_x + self.cars[car_key].length
                end = end_x + self.cars[car_key].length

                for x in range(start, end, step):
                    if self.board[const_y][x] != "0":
                        return False

            self.cars[car_key].row = end_x

            self.cars[car_key].block_count += blocks
            return True

        elif self.cars[car_key].orientation == "V":
            const_x = self.cars[car_key].row
            start_y = self.cars[car_key].col
            end_y = self.cars[car_key].col - blocks

            if blocks < 0:
                end_y = self.cars[car_key].col + -(blocks)
                start = start_y
                end = end_y
                #dit blok heb ik weggehaald omdat dit voorkwam dat de verticale vrachtwagens naar beneden gingen
                # if self.cars[car_key].length == 3:
                #     start += 1
                #     end += 1

                for y in range(start + 1, end + 1, step):
                    if self.board[y][const_x] != "0":
                        return False

            #ik heb hier aangepast dat de start en eind positie verminderd wordt met de lengte van de auto om te voorkomen dat hij zichzelf checkt
            else:
                for y in range(start_y - self.cars[car_key].length, end_y - self.cars[car_key].length, -step):
                    if self.board[y][const_x] != "0":
                        return False

            self.cars[car_key].col = end_y
            self.cars[car_key].block_count += blocks
            return True
        return False

    def check_space(self, car_key):
        # check which spaces are available to move in around the car
        if self.cars[car_key].orientation == "H":
            if self.cars[car_key].length == 3:
                front = self.dimension - self.cars[car_key].row
                behind = -(self.cars[car_key].row) + 1
                output = [x for x in range(behind, front-1) if x != 0]
                return output                
            else:
                front = self.dimension - self.cars[car_key].row
                behind = -(self.cars[car_key].row) + 1
                output = [x for x in range(behind, front) if x != 0]
                return output

        elif self.cars[car_key].orientation == "V":
            if self.cars[car_key].length == 3:
                front = (self.dimension + 1)-self.cars[car_key].col
                behind = -(self.cars[car_key].col)+2
                output = [-(x) for x in range(behind+1, front) if x != 0]
                return output
            else:
                front = (self.dimension + 1)-self.cars[car_key].col
                behind = -(self.cars[car_key].col)+2
                output = [-(x) for x in range(behind, front) if x != 0]
                return output

    def check_win(self):
        # checks if the game is finished by determining the winning position and the position of car X

        # check if car X is placed in winning position
        if self.cars["X"].row == self.win_location or self.move("X", self.win_location - self.cars["X"].row):
            return True
        else:
            return False

    def car_output(self):
        # generates output for check50 after a game is finished
        with open('with_check.csv', 'a', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(["car", "move"])

            for key in self.cars:
                car = key
                move = self.cars[key].block_count

                if self.cars[key].block_count != 0:
                    writer.writerow([car, move])

    def save_board(self, movement, current_board):
        # saves car coordinates of current move in a dictionary
        key = movement
        count = 0
        step = {self.cars[car]: (
            self.cars[car].col, self.cars[car].row, count) for car in self.cars}

        self.version[key] = step

        return self.version

    def empty_saves(self):
        self.version.clear()
        return self.version

    def possible_movements(self):
        possibilities = []
        for key in self.cars:
            move_list = self.check_space(key)
            for move in move_list:

                if self.check_move(key, move):
                    tuple = (key, move)
                    possibilities.append(tuple)
        return possibilities
