from code.algorithms import random_algorithm, unique_moves, short_path, end_point, breadth_first, breadthfirst_prooning
from code.classes import cars, board
import numpy as np
import csv
import time
import plotly.express as px
import pandas as pd
import pyfiglet
import copy

if __name__ == '__main__':
    print("\nRUSH HOUR - Duo Penotti\n")
    

    avgresult = {}
    thresholdlist = []
    results = {}

    bigthreshold = 0
    iteration = 0
    files=["data/Rushhour6x6_1.csv", "data/Rushhour6x6_2.csv", "data/Rushhour6x6_3.csv", "data/Rushhour9x9_4.csv", "data/Rushhour9x9_5.csv", "data/Rushhour9x9_6.csv", "data/Rushhour12x12_7.csv"]
    
    # make instance with game
    for boardfile in files:
        datafile = boardfile
        instance = board.Board(datafile)
        cardic = instance.load_cars(datafile)

        empty_board = instance.create_board()
        instance.load_board(empty_board)

        ep = end_point.End_point(instance, cardic)
    
        while bigthreshold < 10:
            threshold = bigthreshold / 10
            results[threshold] = []
            iteration = 0
            print("\n\n",bigthreshold,"\n\n")
            while iteration < 1:
                print(iteration)
                result = ep.random_run(threshold)[0]
                results[threshold].append(result)

                instancecopy = copy.deepcopy(instance)
                cardic = instancecopy.load_cars(datafile)
                empty_board = instancecopy.create_board()
                instancecopy.load_board(empty_board)

                ep = end_point.End_point(instancecopy, cardic)

                iteration += 1
                
            thresholdlist.append(threshold)

            # calculate avg result for threshold      
            avgresult[threshold] = np.mean(results[threshold])
            
            bigthreshold += 1



        
        with open('ep_optima.csv', mode='a') as opti:
            optimum_writer = csv.writer(opti)
            optimum_writer.writerow([datafile])
            for threshold, result in avgresult.items():
                optimum_writer.writerow([threshold, result])