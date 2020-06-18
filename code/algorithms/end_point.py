from numpy import random
from .random_algorithm import randy
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
        self.empty_board = self.instance_copy.create_board()
        # print(self.instance_copy.load_board(empty_board))

        self.border = self.instance_copy.dimension + 1

        # print(f"border: {self.border}")
        #self.car = input("Which car?\n").upper()
        # print()
        
    def random_run(self, threshold):
        threshold = threshold

        value = 0

        print(f"value = {value}")

        while not self.instance_copy.check_win():
            if value < threshold:
                print("use single run")
                self.single_run()
            else:
                print("use random")
                randy(self.instance_copy, self.cars)
                self.movements += 1
            
            value = random.uniform(0, 1)

        print(f"finished in {self.movements} steps")

    def run(self):
        blocker = {}
        free_cars = []
        checked_cars = []
        last_car = {"auto": ""}

        while not self.instance_copy.check_win():
            if self.is_not_blocked("X") == True:
                self.instance_copy.move("X", 1)

            else:            
                while True:
                    blocker_x = self.is_not_blocked("X")
                    blocker["X"] = blocker_x
                    checked_cars.append("X")
                    
                    lengte = len(checked_cars)
                    # print(f"# of checked cars = {lengte}\n")
                    # print(f"blockers = {blocker}")
                    blocker_copy = blocker.copy()
                    # print(f"cars that should be skipped:  {checked_cars}")

                    for cars in blocker_copy.values():
                        for car in cars:            
                            if car == "edge" or car == True:
                                # niet gebruiken
                                # print(f"{car} skipped")
                                continue

                            if car in checked_cars:
                                # print(f"{car} already checked")
                                continue                    

                            # print(f"\ncar in loop = {car}")
                            
                            if car not in checked_cars:
                                checked_cars.append(car)
                            
                            blockers = self.is_not_blocked(car)
                            
                            if blockers[1] != True:
                                # print(f"added {car} to blockers")
                                blocker[car] = blockers

                            # print(f"blocker update: {blocker}")

                            for blockers in blocker_copy.values():
                                for block in blockers:
                                    if block == "edge" or block == True:
                                        continue
                                    if self.is_not_blocked(block)[0] == True:
                                        if block not in free_cars:
                                            # print(f"added {block} to free cars")
                                            free_cars.append(block)
                                            # print(f"free cars = {free_cars}\n")

                    if len(checked_cars) == lengte:
                        break                    

                if len(free_cars) > 0:
                    while True:
                        # Choose a car randomly from free cars
                        randomcar = random.choice(list(free_cars))

                        # Check movable spaces of the car
                        movementspace = self.instance_copy.check_space(randomcar)

                        # Choose a move randomly
                        randommovement = random.choice(movementspace)

                        if randomcar != last_car["auto"] and self.instance_copy.move(randomcar, randommovement):
                            self.movements += 1
                            # print("making a step")
                            empty_board = self.instance_copy.create_board()
                            print(self.instance_copy.load_board(empty_board))
                            self.instance_copy.check_win()
                            last_car["auto"] = randomcar
                            break              
                
                free_cars.clear()
                checked_cars.clear()
                blocker.clear()
                # print(f"step {self.movements}")


    def single_run(self):
        blocker = {}
        free_cars = []
        checked_cars = []
        last_car = {"auto": ""}

        while True:
            blocker_x = self.is_not_blocked("X")
            blocker["X"] = blocker_x
            checked_cars.append("X")
            
            lengte = len(checked_cars)
            # print(f"# of checked cars = {lengte}\n")
            # print(f"blockers = {blocker}")
            blocker_copy = blocker.copy()
            # print(f"cars that should be skipped:  {checked_cars}")

            for cars in blocker_copy.values():
                for car in cars:            
                    if car == "edge" or car == True:
                        # niet gebruiken
                        # print(f"{car} skipped")
                        continue

                    if car in checked_cars:
                        # print(f"{car} already checked")
                        continue                    

                    # print(f"\ncar in loop = {car}")
                    
                    if car not in checked_cars:
                        checked_cars.append(car)
                    
                    blockers = self.is_not_blocked(car)
                    
                    if blockers[1] != True:
                        # print(f"added {car} to blockers")
                        blocker[car] = blockers

                    # print(f"blocker update: {blocker}")

                    for blockers in blocker_copy.values():
                        for block in blockers:
                            if block == "edge" or block == True:
                                continue
                            if self.is_not_blocked(block)[0] == True:
                                if block not in free_cars:
                                    # print(f"added {block} to free cars")
                                    free_cars.append(block)
                                    # print(f"free cars = {free_cars}\n")

            if len(checked_cars) == lengte:
                break                    

        if len(free_cars) > 0:
            while True:
                # Choose a car randomly from free cars
                randomcar = random.choice(list(free_cars))

                # Check movable spaces of the car
                movementspace = self.instance_copy.check_space(randomcar)

                # Choose a move randomly
                randommovement = random.choice(movementspace)

                if randomcar != last_car["auto"] and self.instance_copy.move(randomcar, randommovement):
                    self.movements += 1
                    print(f"moved {randomcar}")
                    empty_board = self.instance_copy.create_board()
                    print(self.instance_copy.load_board(empty_board))
                    self.instance_copy.check_win()
                    last_car["auto"] = randomcar
                    break              
        
        free_cars.clear()
        checked_cars.clear()
        blocker.clear()
        # print(f"step {self.movements}")

            
    def is_not_blocked(self, car):    
        # returns which car is blocking input car if there is no space to move
        car = car
        # print(f"checking car {car}...")

        if car == "X":
            # check if there is a space available to move car X towards the exit
            space_x = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)
            # print(f"x space = {space_x}")

            # if self.instance_copy.cars["X"].row + 2 == "0": # checkt 1 stap naar rechts + 2 blocks auto lengte
            #     return True
            if space_x.isnumeric():
                return True
            
            else:
                #blocker = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)
                
                return space_x

        else:
            # print(f"orientation = {self.instance_copy.cars[car].orientation}")

            length = self.instance_copy.cars[car].length

            # check if car is oriented horizontally or vertically
            if self.instance_copy.cars[car].orientation == "H":

                # determine columns left & right of car
                left_col = self.instance_copy.cars[car].row - 1
                right_col = self.instance_copy.cars[car].row + length

                # determine board filler left & right of car
                space_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                space_right = self.get_car(right_col, self.instance_copy.cars[car].col)  

                # blocker_left = False
                # blocker_right = False


                # if space_left.isnumeric() and int(blocker_left) > 0:
                #     blocker_left = "edge"
                # if space_right.isnumeric() and int(blocker_right) > 0:
                #     blocker_right = "edge"

                # check if car is facing an open space
                if (space_left.isnumeric() and left_col != 0) and (space_right.isnumeric() and right_col != self.border):
                    return (True, True)

                elif (space_left == str(0) and left_col != 0):
                    blocker = self.get_car(right_col, self.instance_copy.cars[car].col)
                    if blocker.isnumeric() and int(blocker) != 0:
                        blocker = "edge"
                    return (True, blocker)

                elif (space_right == str(0) and right_col != self.border):
                    blocker = self.get_car(left_col, self.instance_copy.cars[car].col)
                    if blocker.isnumeric() and int(blocker) != 0:
                        blocker = "edge"
                    return (True, blocker)

                elif self.get_car(left_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by the wall  on the left
                    blocker_left = "edge"
                    blocker_right = self.get_car(right_col, self.instance_copy.cars[car].col)

                elif self.get_car(right_col, self.instance_copy.cars[car].col) not in self.cars:
                    # blocked by wall on the right                    
                    blocker_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                    blocker_right = "edge"
 
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

                # determine board filler above & below of car
                space_up = self.get_car(self.instance_copy.cars[car].row, row_up)
                
                space_down = self.get_car(self.instance_copy.cars[car].row, row_down)                

                # check if car is facing two open spaces
                if (space_up.isnumeric() and row_up != 0) and (space_down.isnumeric() and row_down != self.border):
                    return (True, True)

                # check if car is facing one open space
                elif (space_up.isnumeric() and row_up != 0):
                    blocker = self.get_car(self.instance_copy.cars[car].row, row_down)
                    if blocker.isnumeric() and int(blocker) != 0:
                        blocker = "edge"
                    return (True, blocker)

                elif (space_down.isnumeric() and row_down != self.border):
                    blocker = self.get_car(self.instance_copy.cars[car].row, row_up)
                    if blocker.isnumeric() and int(blocker) != 0:
                        blocker = "edge"
                    return (True, blocker)

                # check if car is facing two cars or a car and a wall
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
    
