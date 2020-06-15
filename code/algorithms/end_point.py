from numpy import random
import csv
import random
import copy
"""
Algorithm that checks which cars are in the way of the red car and moves the outer ones. 
Probably used best in conjunction with a random algorithm.
"""

# can red car move? (is blocked?)
    # if yes -> move
    # else -> which car is in the way
        # can this car move
        # if yes -> move
        # else -> which car is in the way
            # enz

class End_point():
    def __init__(self, inst, cars):
        movements = 0
        self.cars = cars

        # Copy of the main game instance
        self.instance_copy = copy.deepcopy(inst, self.cars)

        # # print to check
        # empty_board = self.instance_copy.create_board()
        # print(self.instance_copy.load_board(empty_board))

        self.border = self.instance_copy.dimension + 1

        print(f"border: {self.border}")
        self.car = input("Which car?\n").upper()
        print()
        print(f"car {self.car} at {self.instance_copy.cars[self.car].get_position()}")
        

    def run(self, inst, cars):
        if is_blocked("X") is False:
            self.instance_copy.move("X", 1) # of random stap?????

        # klopt nog niet x kan ook 1 blocker returnen
        else:
            blocker["1"] = is_blocked("X")[0]
            blocker["2"] = is_blocked("X")[1]

        for car in blocker:
            if blocker[car] == "edge":
                # doe iets
                pass
            while is_blocked(car) is not False:
                is_blocked(car)

        

    def is_blocked(self):    
        # returns which car is blocking input car if there is no space to move
        car = self.car
        

        if car == "X":
            # check if there is a space available to move car X towards the exit
            if self.instance_copy.cars["X"].row + 2 == "0": # checkt 1 stap naar rechts + 2 blocks auto lengte
                return False
            
            else:
                blocker = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)
                print(f"blocked by {blocker}")
                
                return blocker

        else:
            print(f"orientation = {self.instance_copy.cars[car].orientation}")

            length = self.instance_copy.cars[car].length

            # check if car is oriented horizontally or vertically
            if self.instance_copy.cars[car].orientation == "H":

                # determine columns left & right of car
                left_col = self.instance_copy.cars[car].row - 1
                right_col = self.instance_copy.cars[car].row + length

                # print columns left & right of car as check
                print(f"left col = {left_col}")
                print(f"right col = {right_col}")

                # determine board filler left & right of car
                space_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                space_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)                
                
                print(f"left space = {space_left}")
                print(f"right space = {space_right}")

                # check if car is facing an open space
                if (space_left.isnumeric() and left_col != 0) or (space_right.isnumeric() and right_col != self.border):
                    print("not blocked!")
                    return False

                elif self.get_car(left_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by the wall  on the left
                    blocker_left = "edge"
                    blocker_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)

                elif self.get_car(right_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by wall on the right
                    blocker_right = "edge"
                    blocker_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)

                else:
                    # determine which cars are blocking the sides
                    blocker_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                    blocker_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)
            
                print(f"return left blocker = {blocker_left}")
                print(f"return right blocker = {blocker_right}")

                return (blocker_left, blocker_right)


            
    def get_car(self, x, y):
        # returns which car is located on a specified position on the board
        posx = y
        posy = x
        
        car = self.instance_copy.board[posx][posy]
        return car
    
