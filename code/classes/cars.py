class Car:
    """
    Creates Car objects used to fill the board of the game Rush Hour
    """

    def __init__(self, orientation, row, col, length):
        # initialise car class
        self.orientation = orientation
        self.row = int(row)
        self.col = int(col)
        self.length = int(length)

        self.position = {}
        self.move_count = 0
        self.block_count = 0


    def get_position(self):
        # returns position of car on the board
        self.position["row"] = self.col
        self.position["col"] = self.row # switched up to match the board
        return self.position

    def get_move_count(self):
        # returns the number of times a car has been moved
        return self.move_count

    def get_block_count(self):
        # returns the number of blocks a car has traveled
        return self.block_count
