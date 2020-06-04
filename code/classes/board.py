class Board():
    def __init__(self, source_file):
        self.cars = self.load_cars(source_file)


    def load_cars(self, datafile):
        
        # Open datafile 
        with open(datafile, 'r') as file:
            cars = {}
            reader = csv.DictReader(in_file)
            for row in reader:
                cars[row['name']]

    