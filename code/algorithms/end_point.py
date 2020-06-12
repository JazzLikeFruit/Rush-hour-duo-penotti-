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

        # Copy of the main game instance
        self.instance_copy = copy.deepcopy(inst, cars)

        # print to check
        empty_board = self.instance_copy.create_board()
        print(self.instance_copy.load_board(empty_board))
        
        self.car = input("Which car?\n").upper()
        print()
        print(f"car {self.car} at {self.instance_copy.cars[self.car].get_position()}")

    def run(self, inst, cars):
       if not is_blocked("X"):
           instance_copy.move("X", 1) # of random stap?????
        else:
            for blocker in is_blocked("X"):
                is_blocked(blocker)

    def is_blocked(self):    
        # returns which car is blocking input car if there is no space to move

        car = self.car

        # if self.instance_copy.cars[car].orientation == "H":

        #     # determine board edges
        #     front_edge = self.instance_copy.dimension - self.instance_copy.cars[car].row
        #     back_edge = -(self.instance_copy.cars[car].row) + 1

        #     horizontal_space = [x for x in range(back_edge, front_edge) if x != 0]
        #     #print(f"horizontal space = {horizontal_space}")

        # elif self.instance_copy.cars[car].orientation == "V":
        #     front_edge = (self.instance_copy.dimension + 1)-self.instance_copy.cars[car].col
        #     back_edge = -(self.instance_copy.cars[car].col) + 2

        #     vertical_space = [-(y) for y in range(back_edge, front_edge) if y != 0]
        #     #print(f"vertical space = {vertical_space}")

        if car == "X":
            # check if there is a space available to move car X towards the exit
            if self.instance_copy.cars["X"].row + 2 == "0": # checkt 1 stap naar rechts + 2 blocks auto lengte
                return False
            
            else:
                blocker = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)
                print(f"blocked by {blocker}")
                
                return blocker

        else:
            print(f"checking car {car}...")
            # als er 0 aan de randen is ==> return false (beweeg random in move)
            print(f"orientation = {self.instance_copy.cars[car].orientation}")
            length = self.instance_copy.cars[car].length

            # check if car is oriented horizontally or vertically
            if self.instance_copy.cars[car].orientation == "H":
                left = self.instance_copy.cars[car].row - 1
                right = self.instance_copy.cars[car].row + length

                # print columns left & right of car as check
                print(f"left = {left}")
                print(f"right = {right}")

                # print as a check (remove all 4 lines before final code)
                blocker_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                blocker_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)                
                print(f"left = {blocker_left}")
                print(f"right = {blocker_right}")

                # check if car is facing an open space
                if self.instance_copy.cars[car].row - 1 or self.instance_copy.cars[car].row + length == 0:
                    print("not blocked!")
                    return False

                elif left == instance_copy.board.dimension:
                    # blocked by the wall  on the left
                    blocker_left = "edge"
                    blocker_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)

                elif right == instance_copy.board.dimension:
                    # blocked by wall on the right
                    blocker_right = "edge"
                    blocker_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)

                else:
                    # determine which cars are blocking the sides
                    blocker_left = self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                    blocker_right = self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)
            
                print(f"left = {blocker_left}")
                print(f"right = {blocker_right}")

                return (blocker_left, blocker_right)

            # NOG NIET DE GOEDE COLOMMEN IN DE CODE
            if self.instance_copy.cars[car].orientation == "V":
                up = self.instance_copy.cars[car].col # + modification
                down = self.instance_copy.cars[car].col # + modification

                # print columns left & right of car as check
                print(f"up = {up}")
                print(f"down = {down}")

                # print as a check (remove all 4 lines before final code)
                blocker_up = #self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                blocker_down = #self.get_car(self.instance_copy.cars[car].row + 2, self.instance_copy.cars[car].col)                
                print(f"left = {blocker_left}")
                print(f"right = {blocker_right}")

                # check if car is facing an open space
                if #self.instance_copy.cars[car].row - 1 or self.instance_copy.cars[car].row + length == 0:
                    print("not blocked!")
                    return False

                elif up == instance_copy.board.dimension:
                    # blocked by the wall  on the left
                    blocker_up = "edge"
                    blocker_down = #self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)

                elif down == instance_copy.board.dimension:
                    # blocked by wall on the right
                    blocker_down = "edge"
                    blocker_up = #self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)

                else:
                    # determine which cars are blocking the sides
                    blocker_up = #self.get_car(self.instance_copy.cars[car].row - 1, self.instance_copy.cars[car].col)
                    blocker_down = #self.get_car(self.instance_copy.cars[car].row + length, self.instance_copy.cars[car].col)

                print(f"up = {blocker_up}")
                print(f"down = {blocker_down}")

                return (blocker_up, blocker_down)
            
    def get_car(self, x, y):
        # returns which car is located on a specified position on the board
        posx = y
        posy = x
        
        car = self.instance_copy.board[posx][posy]
        return car
    
