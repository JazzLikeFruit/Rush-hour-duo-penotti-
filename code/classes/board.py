import csv
from cars import Car


class Board():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)

    def load_cars(self, datafile):
        """
        Load the cars of a board 
        """
        # Open datafile
        with open(datafile, 'r') as file:
            cars = {}
            reader = csv.DictReader(file)
            for row in reader:
                cars[row['car']] = Car(
                    row['car'], row['orientation'], row['row'], row['col'], row['length'])

        return cars


if __name__ == '__main__':
    print(Board("data/Rushhour6x6_1.csv").__str__())
