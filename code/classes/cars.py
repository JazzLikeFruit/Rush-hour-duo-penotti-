class Car:
    def __init__(self, name, orientation, row, col, length):
        # initialise car class
        self.name = name
        self.orientation = orientation
        self.row = row
        self.col = col
        self.length = length

    def move(self, blocks):
        # moves the car along the number of blocks depending on orientation
        if self.orientation == "H":
            self.row = self.row + blocks

        elif self.orientation == "V":
            self.col = self.col + blocks

        else:
            return False # nodig in het geval dat er iets niet klopt??

    def position(self):
        # returns position of car on the board
        position["row"] = self.row
        position["col"] = self.col
        return position

