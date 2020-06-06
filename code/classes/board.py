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
        dimension = int(source_file[-7])
        # Creeer een array met nullen op basis van dimensie om vol te zetten met auto's
        boarddummy = np.zeros((dimension+2, dimension+2), int).astype(str)

        boarddummy[0] = '|'  # eerste rij van muren voorzien
        boarddummy[-1] = '|'  # laatste rij van muren voorzien

        for x in boarddummy:
            x[0] = '|'  # eerste kolom van muren voorzien
            x[-1] = '|'  # laatste kolom van muren voorzien

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
            cijfery = self.cars[car_key].row + blocks
            cijferx = 7-self.cars[car_key].col
            #print(cijfery)
            #print(cijferx)
            print(self.board[cijferx][cijfery])

            if self.board[cijferx][cijfery] != "0":
                return False
            self.cars[car_key].row = cijfery
            return True

        elif self.cars[car_key].orientation == "V":

            cijfery = self.cars[car_key].row
            cijferx = 7-(self.cars[car_key].col + blocks)

            #print(cijfery)
            #print(cijferx)
            if self.board[cijferx][cijfery] != "0":
                return False
            self.cars[car_key].col = cijferx
            return True

        else:
            # in case there is an error in the loaded orientation
            return False

        self.cars[car_key].move_count += 1
        self.cars[car_key].block_count += blocks

    def check_space(self, car_key):
        if self.cars[car_key].orientation == "H":
            front = 5-self.cars[car_key].row
            behind = -(self.cars[car_key].row) + 1 
        elif self.cars[car_key].orientation == "V":
            front = 5-self.cars[car_key].col
            behind = -(self.cars[car_key].col) + 1
        return range(behind,front)