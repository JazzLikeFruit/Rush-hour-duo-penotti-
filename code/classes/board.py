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

    def load_board(self, y):
        board = y
        for key, row in self.cars.items():  # loop door input dataframe
            posx = 7-self.cars[key].col
            posy = self.cars[key].row
            board[posx][posy] = board[posx][posy].replace(
                '0', key)  # Vervang 0 met de relevante auto letter
            # check of de auto horizontaal of verticaal is georienteerd om te bepalen waar de volgende letter moet komen
            if self.cars[key].orientation == 'H':
                board[posx][posy+1] = board[posx][posy+1].replace('0', key)
                # check hoe groot de auto is om te bepalen of er nog een derde letter bij moet komen
                if self.cars[key].length == 3:
                    board[posx][posy+2] = board[posx][posy+2].replace('0', key)
            if self.cars[key].orientation == 'V':
                board[posx-1][posy] = board[posx-1][posy].replace('0', key)
                if self.cars[key].length == 3:
                    board[posx-2][posy] = board[posx-2][posy].replace('0', key)
        return board
