from code.algorithms import random_algorithm, unique_moves, short_path, end_point, breadth_first, breadthfirst_prooning
from code.classes import cars, board
from numpy import random
import csv
import time
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import cProfile
import re
import pyfiglet

files = ["data/Rushhour6x6_1.csv", "data/Rushhour6x6_2.csv", "data/Rushhour6x6_3.csv",
         "data/Rushhour9x9_4.csv", "data/Rushhour9x9_5.csv", "data/Rushhour9x9_6.csv", "data/Rushhour12x12_7.csv"]
if __name__ == '__main__':
    # file selection

    print(pyfiglet.figlet_format('Rush Hour', font='slant'))
    print("\nDuo Penotti\n")
    game = input(
        "select game:\n- 1 6x6\n- 2 6x6\n- 3 6x6\n- 4 9x9\n- 5 9x9\n- 6 9x9\n- 7 12x12\n")
    if game == "1":
        datafile = "data/Rushhour6x6_1.csv"
    elif game == "2":
        datafile = "data/Rushhour6x6_2.csv"
    elif game == "3":
        datafile = "data/Rushhour6x6_3.csv"
    elif game == "4":
        datafile = "data/Rushhour9x9_4.csv"
    elif game == "5":
        datafile = "data/Rushhour9x9_5.csv"
    elif game == "6":
        datafile = "data/Rushhour9x9_6.csv"
    elif game == "7":
        datafile = "data/Rushhour12x12_7.csv"
    else:
        print("input invalid")
        raise SystemExit

    if game.lower() != "all":
        print(f"Board {game} chosen")
        # load chosen board
        instance = board.Board(datafile)
        empty_board = instance.create_board()
        cardic = instance.load_cars(datafile)

        print(instance.load_board(empty_board))
        print("\n====================================\n")
        print("Choose an algorithm to solve the puzzel with by typing the number :")

        algorithms = {'1': 'Random Algorithm', '2': 'Unique moves Algorithm',
                      '3': 'Optimized moves Algorithm', '4': 'End Point Algorithm', '5': 'Breadth first plus prooning', 'all': '5 runs of all algorithms inculding a visualisation'}

        for alogrithm in algorithms:
            print(f"- {alogrithm}: {algorithms[alogrithm]}")

        while True:

            print("\nEnter your choice:")
            inputalgorithm = input().lower()
            if inputalgorithm not in algorithms:
                print('Incorrect algorithm select one of the following: ')

            elif inputalgorithm in algorithms and inputalgorithm != 'all':

                print('\nLoading', algorithms[inputalgorithm], '...\n')
                break
            elif inputalgorithm == 'all':
                print('\nLoading sample of all algorithms...\n')
                break
        if inputalgorithm == '1':
            result = random_algorithm.randy(instance, cardic)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '2':
            # try/except implemented because this function has a lot of recursion
            try:
                result = unique_moves.unique(instance, cardic)
                print(result[0])
                print(result[1])
            except RecursionError as re:
                print(
                    'Recursion depth reached, try again if you have faith but this algorithm struggles with large boards')

        elif inputalgorithm == '3':
            result = short_path.short(instance, cardic)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '4':
            # threshold for random movement can be manually selected
            threshold = input(
                "how often should end-point be used?\nenter value between 0-1\n")
            while True:
                if float(threshold) > 1 or float(threshold) < 0:
                    threshold = input("choose a number between 0-0.9\n")
                if float(threshold) < 1 and float(threshold) > 0:
                    break
            ep = end_point.End_point(instance, cardic)
            result = ep.random_run(threshold)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '5':
            bfp = breadthfirst_prooning.BreathFirst_P(instance)
            # cProfile.run('bfp.run()')
            result = bfp.run()

            print(result[0])
            print(result[1])
        elif inputalgorithm == 'all':
            # automatically runnning multiple iterations of all functions (with some exceptions handled in a user friendly manner)
            times = []
            results = []
            algo = []
            iterations = 0
            df = pd.DataFrame()
            resultdic = {}
            boardfile = datafile
            while iterations < 21:
                instance = board.Board(boardfile)
                empty_board = instance.create_board()
                cardic = instance.load_cars(boardfile)
                instance.load_board(empty_board)

                start = time.time()
                if iterations < 5:
                    startiteration = time.time()
                    result = random_algorithm.randy(instance, cardic)
                    times.append(time.time()-startiteration)
                    results.append(result[0])
                    algo.append('Random')
                    iterations += 1
                    print('Random')

                if 4 < iterations < 10:
                    startiteration = time.time()
                    result = short_path.short(instance, cardic)
                    times.append(time.time()-startiteration)
                    results.append(result[0])
                    algo.append('Optimized')
                    iterations += 1
                    print('Optimized')

                if 9 < iterations < 15:
                    try:
                        startiteration = time.time()
                        result = unique_moves.unique(instance, cardic)
                        times.append(time.time()-startiteration)
                        results.append(result[0])
                        algo.append('Unique')
                        iterations += 1
                        print('Unique')
                    except RecursionError as re:
                        iterations = 15
                        print(
                            'Unique reached recursion depth and algorithm was skipped')

                if 14 < iterations < 16 and datafile in files[:4]:
                    startiteration = time.time()
                    bfp = breadthfirst_prooning.BreathFirst_P(instance, cardic)
                    result = bfp.run()
                    times.append(time.time()-startiteration)
                    results.append(result[0])
                    algo.append('Breadth Pruned')
                    iterations += 1
                    print('Breadth Pruned')
                # prevent breadth first with prooning from running on the most difficult three boards
                if 14 < iterations < 16 and datafile not in files[:4]:
                    print(
                        'This board has not been possible to solve with this algorithm thus far')
                    iterations += 1

                if 15 < iterations:
                    startiteration = time.time()
                    ep = end_point.End_point(instance, cardic)
                    result = ep.random_run(0.7)
                    times.append(time.time()-startiteration)
                    results.append(result[0])
                    algo.append('End')
                    iterations += 1
                    print('End')

            # building of dictionary and dataframe
            resultdic['Iteration'] = list(range(len(times)))
            resultdic['Time'] = times
            resultdic['Movements'] = results
            resultdic['Algorithm'] = algo

            dfnew = pd.DataFrame.from_dict(resultdic)

            # plotting of the sample of algorithms
            fig1 = px.histogram(dfnew,
                                x="Algorithm", y="Movements", color="Algorithm", histfunc="avg")
            fig1.show()
            fig2 = px.histogram(dfnew,
                                x="Algorithm", y="Time", color="Algorithm", histfunc="avg")
            fig2.show()
