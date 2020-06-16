from numpy import random
import csv
import random
import copy
"""
Algorithm that checks which cars are in the way of the red car and moves the outer ones. 
Probably used best in conjunction with a random algorithm.
"""


class End_point():
    def __init__(self, inst, cars):
        self.movements = 0
        self.cars = cars

        # Copy of the main game instance
        self.instance_copy = copy.deepcopy(inst, self.cars)

        # # print to check
        # empty_board = self.instance_copy.create_board()
        # print(self.instance_copy.load_board(empty_board))

        self.border = self.instance_copy.dimension + 1

        print(f"border: {self.border}")
        #self.car = input("Which car?\n").upper()
        print()
        

    def run(self):
        # can red car move? (is blocked?)
            # if yes -> move
            # else -> which car is in the way
                # can this car move
                # if yes -> move
                # else -> which car is in the way
                    # enz

        blocker = {}
        free_cars = []
        checked_cars = []

        while not self.instance_copy.check_win():
            
            if self.is_not_blocked("X") == True:
                self.instance_copy.move("X", 1) # of random stap?????

            else:
                blocker_x = self.is_not_blocked("X")

                blocker["1"] = blocker_x
                blocker["2"] = None
                # nog geen blocker 2

                while True:
                    blocker_copy=blocker
                    for car in blocker_copy.values():
                        print(f"car in loop = {car}")
                        
                        if car == "edge":
                            # niet gebruiken
                            continue

                        blockers = self.is_not_blocked(car)

                        blocker["1"] = blockers[0]
                        blocker["2"] = blockers[1]

                        print(f"{blocker}")

                        for block in blocker.values():
                            if block == "edge":
                                continue
                            if self.is_not_blocked(block) == True:
                                if block not in free_cars:
                                    free_cars.append(block)
                                break

                while True:
                    # Choose a car randomly from free cars
                    randomcar = random.choice(list(free_cars))

                    # Check movable spaces of the car
                    movementspace = self.instance_copy.check_space(randomcar)

                    # Choose a move randomly
                    randommovement = random.choice(movementspace)

                    if self.instance_copy.move(randomcar, randommovement):
                        self.movements+=1
                        break

                free_cars.clear()
                checked_cars.clear()
                print(self.movements)
            
    def is_not_blocked(self, car):    
        # returns which car is blocking input car if there is no space to move
        car = car
        # print(f"checking car {car}...")

        if car == "X":
            # check if there is a space available to move car X towards the exit
            if self.instance_copy.cars["X"].row + 2 == "0": # checkt 1 stap naar rechts + 2 blocks auto lengte
                return True
            
            else:
                blocker = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)
                # print(f"blocked by {blocker}")
                
                return blocker

        else:
            # print(f"orientation = {self.instance_copy.cars[car].orientation}")

            length = self.instance_copy.cars[car].length

            # check if car is oriented horizontally or vertically
            if self.instance_copy.cars[car].orientation == "H":

                # determine columns left & right of car
                left_col = self.instance_copy.cars[car].row - 1
                right_col = self.instance_copy.cars[car].row + length

                # print columns left & right of car as check
                # print(f"left col = {left_col}")
                # print(f"right col = {right_col}")

                # determine board filler left & right of car
                space_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                space_right = self.get_car(right_col, self.instance_copy.cars[car].col)                
                
                # print(f"left space = {space_left}")
                # print(f"right space = {space_right}")

                # check if car is facing an open space
                if (space_left.isnumeric() and left_col != 0) or (space_right.isnumeric() and right_col != self.border):
                    # print("not blocked!")
                    return True

                elif self.get_car(left_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by the wall  on the left
                    blocker_left = "edge"
                    blocker_right = self.get_car(right_col, self.instance_copy.cars[car].col)

                elif self.get_car(right_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by wall on the right
                    blocker_right = "edge"
                    blocker_left = self.get_car(left_col, self.instance_copy.cars[car].col)

                else:
                    # determine which cars are blocking the sides
                    blocker_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                    blocker_right = self.get_car(right_col, self.instance_copy.cars[car].col)
            
                # print(f"return left blocker = {blocker_left}")
                # print(f"return right blocker = {blocker_right}")

                return (blocker_left, blocker_right)

            elif self.instance_copy.cars[car].orientation == "V":

                # determine rows above & below of car
                row_up = self.instance_copy.cars[car].col - length
                row_down = self.instance_copy.cars[car].col + 1

                # print columns above & below of car as check
                # print(f"upper row = {row_up}")
                # print(f"down row = {row_down}")

                # determine board filler above & below of car
                space_up = self.get_car(self.instance_copy.cars[car].row, row_up)
                space_down = self.get_car(self.instance_copy.cars[car].row, row_down)                
                
                # print(f"upper space = {space_up}")
                # print(f"down space = {space_down}")

                # check if car is facing an open space
                if (space_up.isnumeric() and row_up != 0) or (space_down.isnumeric() and row_down != self.border):
                    # print("not blocked!")
                    return True

                elif self.get_car(self.instance_copy.cars[car].row, row_up) not in self.cars:
                    # blocked by the wall above
                    blocker_up = "edge"
                    blocker_down = self.get_car(self.instance_copy.cars[car].row, row_down)

                elif self.get_car(self.instance_copy.cars[car].row, row_down) not in self.cars:
                    # blocked by wall below
                    blocker_down = "edge"
                    blocker_up = self.get_car(self.instance_copy.cars[car].row, row_up)

                else:
                    # determine which cars are blocking the sides
                    blocker_up = self.get_car(self.instance_copy.cars[car].row, row_up)
                    blocker_down = self.get_car(self.instance_copy.cars[car].row, row_down)
            
                # print(f"return upper blocker = {blocker_up}")
                # print(f"return down blocker = {blocker_down}")

                return (blocker_up, blocker_down)


            
    def get_car(self, x, y):
        # returns which car is located on a specified position on the board
        posx = y
        posy = x
        
        car = self.instance_copy.board[posx][posy]
        return car
    
