class Car:
    def __init__(self, name, orientation, row, col, length):
        # initialise car class
        self.name = name
        self.orientation = orientation
        self.row = int(row)
        self.col = int(col)
        self.length = int(length)

        self.position = {}
        self.move_count = 0

    def is_red(self):
        # check if this car is the red car
        if self.name == "X":
            return True
        else:
            return False

    def move(self, blocks):
        # moves the car along the number of blocks depending on orientation
        if self.orientation == "H":
            self.row = self.row + blocks

        elif self.orientation == "V":
            self.col = self.col + blocks

        else:
            # in case there is an error in the loaded orientation
            return False

        self.move_count += 1

    def get_name(self):
        # returns the name of the car
        return self.name

    def get_position(self):
        # returns position of car on the board
        self.position["row"] = self.row
        self.position["col"] = self.col
        return self.position

    def get_move_count(self):
        # returns the number of times a car has been moved
        return self.move_count