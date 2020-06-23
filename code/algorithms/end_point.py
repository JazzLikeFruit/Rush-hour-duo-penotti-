from numpy import random
import random
import copy
"""
Algorithm that checks which cars are in the way of the red car and moves the outer ones. 
Is used in conjunction with a random algorithm based on a user-supplied threshold value
"""


class End_point():
    def __init__(self, inst, cars):
        self.movements = 0
        self.cars = cars
        self.carlist = list(self.cars)

        # Copy the main game instance
        self.instance_copy = copy.deepcopy(inst, self.cars)

        # Create board from copy
        self.empty_board = self.instance_copy.create_board()

        # Define edge of the board
        self.border = self.instance_copy.dimension + 1

        
    def random_run(self, threshold):
        # Combines the end point algorithm with the random algorithm based on a threshold value
        threshold = float(threshold)

        # Always start with end point algorithm
        value = 0

        while not self.instance_copy.check_win():

            # Use end point algorithm if random value falls within threshold range
            if value < threshold:
                self.single_run()

            # Use random algorithm if random value falls out of threshold range
            else:
                while True:
                    # Choose a car randomly from free cars
                    randomcar = random.choice(list(self.carlist))

                    # Check movable spaces of the car
                    movementspace = self.instance_copy.check_space(randomcar)

                    # Choose a move randomly
                    randommovement = random.choice(movementspace)

                    # Carry out the move if the car is different than the last used car and the move is valid
                    if self.instance_copy.move(randomcar, randommovement):
                        self.movements += 1

                        # Reload board and check if win has been achieved
                        empty_board = self.instance_copy.create_board()
                        self.instance_copy.load_board(empty_board)
                        break

            # Get other random value
            value = random.uniform(0, 1)

        # Return winning board
        empty_board = self.instance_copy.create_board()
        result = self.instance_copy.load_board(empty_board)
        return (self.movements, result)


    def single_run(self):
        # Looks through the cars blocking car X and performs a single move with one of the unblocked cars
        blocker = {}
        free_cars = []
        checked_cars = []
        last_car = {"auto": ""}

        while True:
            # Keeps checking blocked cars until no new cars are found
            blocker_x = self.is_not_blocked("X")

            # Move X if X is free
            if blocker_x == True:
                self.instance_copy.move("X", 1)
                break

            blocker["X"] = blocker_x
            checked_cars.append("X")
            
            # Make copy of dictionary and determine amount of checked cars to use in loop
            lengte = len(checked_cars)
            blocker_copy = blocker.copy()

            # Check which cars are blocking the cars in the blocker dictionary
            for cars in blocker_copy.values():
                for car in cars:    

                    # Skip values that are not car names        
                    if car == "edge" or car == True:
                        continue
                    
                    # Skip cars that already have been checked
                    checked_set = set(checked_cars)
                    if car in checked_set:
                        continue                    
                    
                    # Add new car to checked car list
                    checked_cars.append(car)
                    
                    # Determine if current car is blocked
                    blockers = self.is_not_blocked(car)
                    
                    # If car is blocked add blockers to the blocker dictionary
                    if blockers[1] != True:
                        blocker[car] = blockers

                    # Determine if current car is able to move
                    for blockers in blocker_copy.values():
                        for block in blockers:
                            if block == "edge" or block == True:
                                continue

                            # If car can move add to the list of moveable cars
                            if self.is_not_blocked(block)[0] == True:
                                if block not in free_cars:
                                    free_cars.append(block)

            # Break out of loop if no new cars are added to the checked cars list
            if len(checked_cars) == lengte:
                break                    

        # Make a move if any cars are able to
        if len(free_cars) > 0:

            # Keep trying to make a move until a succesfull one is achieved
            while True:

                # Choose a car randomly from free cars
                randomcar = random.choice(list(free_cars))

                # Check movable spaces of the car
                movementspace = self.instance_copy.check_space(randomcar)

                # Choose a move randomly
                randommovement = random.choice(movementspace)

                # Carry out the move if the car is different than the last used car and the move is valid
                if randomcar != last_car["auto"] and self.instance_copy.move(randomcar, randommovement):
                    self.movements += 1

                    # Reload board and check if win has been achieved
                    empty_board = self.instance_copy.create_board()
                    self.instance_copy.load_board(empty_board)
                    self.instance_copy.check_win()

                    # Save name of the moved car
                    last_car["auto"] = randomcar
                    break              
        
        # Clear out the lists & dictionary for the next iteration
        free_cars.clear()
        checked_cars.clear()
        blocker.clear()

            
    def is_not_blocked(self, car):    
        # Returns which car is blocking input car if there is no space to move
        car = car

        if car == "X":
            # Check if there is a space available to move car X towards the exit
            space_x = self.get_car(self.instance_copy.cars["X"].row + 2, self.instance_copy.cars["X"].col)

            # Return True or the car that is blocking X
            if space_x.isnumeric():
                # Return True if X is facing 0 on th board
                return True
            
            else:
                return space_x

        else:
            # Check for the other cars if they are blocked

            length = self.instance_copy.cars[car].length

            # Determine if car is oriented horizontally or vertically
            if self.instance_copy.cars[car].orientation == "H":

                # Determine columns left & right of car
                left_col = self.instance_copy.cars[car].row - 1
                right_col = self.instance_copy.cars[car].row + length

                # Determine board filler left & right of car
                space_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                space_right = self.get_car(right_col, self.instance_copy.cars[car].col)  

                # Check if car is completely free
                if (space_left.isnumeric() and left_col != 0) and (space_right.isnumeric() and right_col != self.border):
                    return (True, True)

                # Check if car is free on one side
                elif (space_left == str(0) and left_col != 0):
                    blocker = self.get_car(right_col, self.instance_copy.cars[car].col)
                    if blocker == "|":
                        blocker = "edge"
                    return (True, blocker)

                elif (space_right == str(0) and right_col != self.border):
                    blocker = self.get_car(left_col, self.instance_copy.cars[car].col)
                    if blocker == "|":
                        blocker = "edge"
                    return (True, blocker)

                # Check if car is blocked on both sides
                elif self.get_car(left_col, self.instance_copy.cars[car].col) not in self.cars:

                    # Blocked by the wall  on the left
                    blocker_left = "edge"
                    blocker_right = self.get_car(right_col, self.instance_copy.cars[car].col)

                elif self.get_car(right_col, self.instance_copy.cars[car].col) not in self.cars:

                    # Blocked by wall on the right                    
                    blocker_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                    blocker_right = "edge"
 
                else:
                    # Determine which cars are blocking both sides
                    blocker_left = self.get_car(left_col, self.instance_copy.cars[car].col)
                    blocker_right = self.get_car(right_col, self.instance_copy.cars[car].col)
        
                return (blocker_left, blocker_right)

            elif self.instance_copy.cars[car].orientation == "V":

                # Determine rows above & below of car
                row_up = self.instance_copy.cars[car].col - length
                row_down = self.instance_copy.cars[car].col + 1

                # Determine board filler above & below of car
                space_up = self.get_car(self.instance_copy.cars[car].row, row_up)
                space_down = self.get_car(self.instance_copy.cars[car].row, row_down)                

                # Check if car is completely free
                if (space_up.isnumeric() and row_up != 0) and (space_down.isnumeric() and row_down != self.border):
                    return (True, True)

                # Check if car is free on one side
                elif (space_up.isnumeric() and row_up != 0):
                    blocker = self.get_car(self.instance_copy.cars[car].row, row_down)
                    if blocker == "|":
                        blocker = "edge"
                    return (True, blocker)

                elif (space_down.isnumeric() and row_down != self.border):
                    blocker = self.get_car(self.instance_copy.cars[car].row, row_up)
                    if blocker == "|":
                        blocker = "edge"
                    return (True, blocker)

                # Check if car is blocked on both sides
                elif self.get_car(self.instance_copy.cars[car].row, row_up) not in self.cars:

                    # Blocked by the wall above
                    blocker_up = "edge"
                    blocker_down = self.get_car(self.instance_copy.cars[car].row, row_down)

                elif self.get_car(self.instance_copy.cars[car].row, row_down) not in self.cars:

                    # Blocked by wall below
                    blocker_down = "edge"
                    blocker_up = self.get_car(self.instance_copy.cars[car].row, row_up)

                else:
                    # determine which cars are blocking both sides
                    blocker_up = self.get_car(self.instance_copy.cars[car].row, row_up)
                    blocker_down = self.get_car(self.instance_copy.cars[car].row, row_down)

                return (blocker_up, blocker_down)
            
    def get_car(self, x, y):
        # Returns which car or board filler is located on a specified position on the board
        posx = y
        posy = x
        
        car = self.instance_copy.board[posx][posy]
        return car
    
