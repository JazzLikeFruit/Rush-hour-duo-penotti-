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

        # Define dimension based on name source file
        self.dimension = int(re.search(r"\d+", source_file)[0])

        self.win_location = self.dimension - 1

    def load_cars(self, datafile):
        # Load cars dictionary from datafile input
        number = int(re.search(r"\d+", datafile)[0]) + 1

        with open(datafile, 'r') as file:
            cars = {}
            reader = csv.DictReader(file)

            # Loop through input file to add cars to dictionary
            for row in reader:
                cars[row['car']] = Car(
                    row['orientation'], row['row'],  (number - int(row['col'])), row['length'])  # Functie om het dummy bord op basis van de input van auto's te voorzien
        return cars

    def create_board(self):
        # Creates board as an array filled with 0s based on dimension
        boarddummy = np.zeros(
            (self.dimension + 2, self.dimension + 2), int).astype(str)

        for x in range(len(boarddummy[0])):
            boarddummy[x][0] = '|'
            boarddummy[x][-1] = '|'
            boarddummy[0][x] = '|'
            boarddummy[-1][x] = '|'
        boarddummy[(len(boarddummy) - int(len(boarddummy) / 2) - 1)
                   ][-1] = '.'  # Creates board exit with '.'
        return boarddummy

    def load_board(self, empty_board):
        self.board = empty_board

        # Loop through cars dictionary to fill board
        for key, row in self.cars.items():
            posx = self.cars[key].col
            posy = self.cars[key].row

            # Replace 0s on board with car name chars
            self.board[posx][posy] = self.board[posx][posy].replace(
                '0', key)

            # Determine car orientation to place car correctly on the board
            if self.cars[key].orientation == 'H':
                self.board[posx][posy +
                                 1] = self.board[posx][posy + 1].replace('0', key)

                # Determine car size and add a block if the car length = 3
                if self.cars[key].length == 3:
                    self.board[posx][posy +
                                     2] = self.board[posx][posy + 2].replace('0', key)
                continue

            # Place vertical cars on the board
            self.board[posx-1][posy] = self.board[posx -
                                                  1][posy].replace('0', key)
            if self.cars[key].length == 3:
                self.board[posx-2][posy] = self.board[posx -
                                                      2][posy].replace('0', key)

        return self.board

    def check_move(self, car_key, blocks):

        # Moves the car along the number of blocks depending on orientation
        if self.cars[car_key].orientation == "H":
            const_y = self.cars[car_key].col
            end_x = self.cars[car_key].row + blocks
            start_x = self.cars[car_key].row

            # Determine if the car moves in positive or negative direction
            if blocks < 0:

                for x in range(start_x - 1, end_x - 1, -1):
                    if self.board[const_y][x] != "0":
                        return False
                return True
            
            # Add car movement in positive direction
            start = start_x + self.cars[car_key].length
            end = end_x + self.cars[car_key].length

            # Check if movement is valid 
            for x in range(start, end):
                if self.board[const_y][x] != "0":
                    return False
            return True
        
        # Check movement for positive cars 
        const_x = self.cars[car_key].row
        start_y = self.cars[car_key].col
        end_y = self.cars[car_key].col - blocks

        # Check if movement is positive 
        if blocks < 0:
            end_y = self.cars[car_key].col + -(blocks)
            start = start_y
            end = end_y

            # Check movement of car 
            for y in range(start + 1, end + 1):
                if self.board[y][const_x] != "0":
                    return False
            return True

        for y in range(start_y - self.cars[car_key].length, end_y - self.cars[car_key].length, -1):
            if self.board[y][const_x] != "0":
                return False
        return True

    # Make movement 
    def move(self, car_key, blocks):

        # Check if movement is valid 
        if self.check_move(car_key, blocks):
            if self.cars[car_key].orientation == 'H':
                self.cars[car_key].row = self.cars[car_key].row + blocks
                self.cars[car_key].block_count += blocks
                return True
            
            # Move horizontal car 
            self.cars[car_key].col = self.cars[car_key].col - blocks
            self.cars[car_key].block_count += blocks
            return True
        return False

    def check_space(self, car_key):
        # Check which spaces are available to move in around the car
        if self.cars[car_key].orientation == "H":
            if self.cars[car_key].length == 3:
                front = self.dimension - self.cars[car_key].row
                behind = -(self.cars[car_key].row) + 1
                output = [x for x in range(behind, front-1) if x != 0]
                return output
            
            # Check space for vertical cars
            front = self.dimension - self.cars[car_key].row
            behind = -(self.cars[car_key].row) + 1
            output = [x for x in range(behind, front) if x != 0]
            return output
        
        # Check size of car and ditermine space 
        if self.cars[car_key].length == 3:
            front = (self.dimension + 1)-self.cars[car_key].col
            behind = -(self.cars[car_key].col)+2
            output = [-(x) for x in range(behind+1, front) if x != 0]
            return output

        front = (self.dimension + 1)-self.cars[car_key].col
        behind = -(self.cars[car_key].col)+2
        output = [-(x) for x in range(behind, front) if x != 0]
        return output
    
    # Check if car X is placed in winning position
    def check_win(self):
        return any((self.cars["X"].row == self.win_location, self.move("X", self.win_location - self.cars["X"].row)))

    # Generates output for check50 after a game is finished
    def car_output(self):
        with open('ouput.csv', 'a', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(["car", "move"])

            # Loop through keys and record movements 
            for key in self.cars:
                move = self.cars[key].block_count

                if self.cars[key].block_count != 0:
                    writer.writerow([key, move])

    # Saves car coordinates of current move in a dictionary
    def save_board(self, movement, current_board):
        
        key = movement
        count = 0
        step = {self.cars[car]: (
            self.cars[car].col, self.cars[car].row, count) for car in self.cars}

        self.version[key] = step

        return self.version

    # Reset the saved boards
    def empty_saves(self):
        self.version.clear()
        return self.version
    
    # Return list with possible movements 
    def possible_movements(self):
        possibilities = []
        for key in self.cars:
            move_list = self.check_space(key)
            for move in move_list:
                if self.check_move(key, move):
                    tuple = (key, move)
                    possibilities.append(tuple)
        return possibilities
