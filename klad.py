def check_space(self, car_key):
    # check which spaces are available to move in around the car
    if self.cars[car_key].orientation == "H":
        front = self.dimension - self.cars[car_key].row
        behind = -(self.cars[car_key].row) + 1
----------------------------------------------------------------------
        output = [x for x in range(behind, front) if x != 0]
        # which means
        output=[]
        for x in range(behind,front):
            if x!=0:
                output.append(x)
        return output


# from move()
----------------------------------------------------------------------
# if H -
const_y = self.cars[car_key].col
end_x = self.cars[car_key].row + blocks
start_x = self.cars[car_key].row

for x in range(start_x - 1, end_x - 1, -step):
    if self.board[const_y][x] != "0":
        return False

# if H +
start = start_x + self.cars[car_key].length
end = end_x + self.cars[car_key].length

for x in range(start, end, step):
    if self.board[const_y][x] != "0":
        return False
----------------------------------------------------------------------
# if V +
for y in range(start_y - 2, end_y - 2, -step):
    if self.board[y][const_x] != "0":
        return False

#if V -
const_x = self.cars[car_key].row
start_y = self.cars[car_key].col
end_y = self.cars[car_key].col - blocks

if blocks < 0:
    end_y = self.cars[car_key].col + -(blocks)
    start = start_y
    end = end_y

    if self.cars[car_key].length == 3:
        start += 1
        end += 1

    for y in range(start + 1, end + 1, step):
        if self.board[y][const_x] != "0":
            return False
----------------------------------------------------------------------


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

----------------------------------------------------------------------
# VERTICAL CHECK
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