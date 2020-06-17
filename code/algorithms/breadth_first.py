import copy


class Breathfirst():
    """
    A Breath First algorithm that finds the solution with the least ammount of steps. 
    """

    def __init__(self, instance, carslist):
        self.instance_copy = instance
        self.cars = carslist

        self.queue = []
        # Returns a number of movements

    def get_next_state(self):
        return self.queue.pop(0)

    def build_children(self, instance, initial_movement):
        move_list = []
        move_list.extend(initial_movement)

        for movement in instance.possible_movements():
            list = move_list
            list.append(movement)
            self.queue.append(list)

    def run(self):

        first_momvements = self.instance_copy.possible_movements()
        for movement in first_momvements:
            self.queue.append(
                list(tuple(movement, first_momvements[movement])))

        while self.queue:
            instance = copy.deepcopy(self.instance_copy)
            count = 0

            # get next movement from queue
            movement = self.get_next_state()

            # Check if queue is not empty
            if movement is not None:

                # Make movement
                for move in movement:

                    # Use values in tuple
                    for key, value in move:
                        instance.move(key, value)
                        count += 1

                # Check win
                if instance.check_win():
                    return print(f'Solution found in {count} moves')

                else:
                    self.build_children(instance, movement)
                    print(self.queue)
