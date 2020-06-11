from code.classes import cars, board
import random

class Random():
    def __init__(self, sourcefile):
        datafile = sourcefile
        self.instance = board.Board(datafile)
        self.cardic = self.instance.load_cars(datafile)
        
    def random_move(self):
        randomcar = random.choice(list(self))
        movementspace = self.instance.check_space(randomcar)
        randommovement = random.choice(movementspace)
        return (randomcar, randommovement)