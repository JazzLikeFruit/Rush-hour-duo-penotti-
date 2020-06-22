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

files = ["data/Rushhour6x6_1.csv", "data/Rushhour6x6_2.csv", "data/Rushhour6x6_3.csv",
         "data/Rushhour9x9_4.csv", "data/Rushhour9x9_5.csv", "data/Rushhour9x9_6.csv", "data/Rushhour12x12_7.csv"]
if __name__ == '__main__':
    print("\nRUSH HOUR - Duo Penotti\n")
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
    elif game.lower() == "all":
        # optie om alle algoritmes x aantal keer te laten draaien en de data te verzmalen in een diagram / csv
        iterations = []
        times = []
        results = []
        algo = []
        df = pd.DataFrame()
        for boardfile in files:
            instance = board.Board(boardfile)
            empty_board = instance.create_board()
            cardic = instance.load_cars(boardfile)
            instance.load_board(empty_board)

            resultdic = {}
            start = time.time()
            while len(iterations) < 6:
                startiteration = time.time()
                result = random_algorithm.randy(instance, cardic)
                times.append(time.time()-startiteration)
                results.append(result[0])
                algo.append('Random')
                iterations.append(len(iterations)+1)

            print('Random')
            uniquedic = {}
            start = time.time()
            while len(iterations) < 11:
                startiteration = time.time()
                result = unique_moves.unique(instance, cardic)
                times.append(time.time()-startiteration)
                results.append(result[0])
                algo.append('Unique')
                iterations.append(len(iterations)+1)

            print('Unique')
            shortdic = {}
            start = time.time()
            while len(iterations) < 16:
                startiteration = time.time()
                result = short_path.unique(instance, cardic)
                times.append(time.time()-startiteration)
                results.append(result[0])
                algo.append('Short')
                iterations.append(len(iterations)+1)

            print('Short')
            enddic = {}
            start = time.time()
            while len(iterations) < 21:
                startiteration = time.time()
                ep = end_point.End_point(instance, cardic)
                ep.random_run(0.5)
                times.append(time.time()-startiteration)
                results.append(result[0])
                algo.append('End')
                iterations.append(len(iterations)+1)

            print('End')
            breadthprunedic = {}
            start = time.time()
            while len(iterations) < 26:
                startiteration = time.time()
                bfp = breadthfirst_prooning.BreathFirst_P(instance)
                result = bfp.run()
                times.append(time.time()-startiteration)
                results.append(result[0])
                algo.append('Breadth Prune')
                iterations.append(len(iterations)+1)
                print(len(iterations)+1)
            print('Breadth Prune')

            # breadthdic = {}
            # start = time.time()
            # while len(iterations) < 26:
            #     startiteration = time.time()
            #     bf = breadth_first.BreathFirst(instance)
            #     result = bf.run()
            #     times.append(time.time()-startiteration)
            #     results.append(result[0])
            #     algo.append('Breadth')
            #     iterations.append(len(iterations)+1)

            # print ('Breadth')

            # bouwen van dictioanary en dataframe
            resultdic['Iteration'] = iterations
            resultdic['Time'] = times
            resultdic['Movements'] = results
            resultdic['Algorithm'] = algo
            resultdic['Datafile'] = boardfile
            dfnew = pd.DataFrame.from_dict(resultdic)
            # berekenen van gemiddeldes
            dfnew['Avg Move'] = dfnew.groupby(['Algorithm', 'Datafile'])['Movements'].transform(
                'mean').round().astype(int)
            dfnew['Avg Time'] = dfnew.groupby(['Algorithm', 'Datafile'])[
                'Time'].transform('mean').round(2)
            df = df.append(dfnew)
        print(df)
        # plotten
        fig1 = px.histogram(df,
                            x="Algorithm", y="Movements", color="Algorithm", histfunc="avg", facet_col="Datafile", facet_col_wrap=4)
        fig1.show()
        fig2 = px.histogram(df,
                            x="Algorithm", y="Time", color="Algorithm", histfunc="avg", facet_col="Datafile", facet_col_wrap=4)
        fig2.show()
    else:
        print("input invalid")
        raise SystemExit

    if game.lower() != "all":
        print(f"Board {game} chosen")
        instance = board.Board(datafile)
        empty_board = instance.create_board()
        cardic = instance.load_cars(datafile)

        print(instance.load_board(empty_board))
        print("\n====================================\n")
        print("Choose an algorithm to solve the puzzel with by typing the number :")

        algorithms = {'1': 'Random Algorithm', '2': 'Unique moves Algorithm',
                      '3': 'Optimized moves Algorithm', '4': 'End Point Algorithm', '5': 'Breadth first algorithm', '6': 'Breadth first plus prooning'}

        for alogrithm in algorithms:
            print(f"- {alogrithm}: {algorithms[alogrithm]}")

        while True:

            print("\nEnter your choice:")
            inputalgorithm = input().lower()
            if inputalgorithm not in algorithms:
                print('Incorrect algorithm select one of the following: ')

            else:

                print('\nLoading', algorithms[inputalgorithm], '...\n')
                break

        if inputalgorithm == '1':
            result = random_algorithm.randy(instance, cardic)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '2':
            result = unique_moves.unique(instance, cardic)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '3':
            result = short_path.unique(instance, cardic)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '4':
            threshold = input(
                "how often should end-point be used?\nenter value between 0-1\n")
            while True:
                if float(threshold) > 1 or float(threshold) < 0:
                    threshold = input("choose a number between 0-1\n")
                if float(threshold) < 1 and float(threshold) > 0:
                    break
            ep = end_point.End_point(instance, cardic)
            resutl = ep.random_run(threshold)
            print(result[0])
            print(result[1])

        elif inputalgorithm == '5':
            bf = breadth_first.BreathFirst(instance)
            result = bf.run()
            print(result[0])
            print(result[1])

        elif inputalgorithm == '6':
            bfp = breadthfirst_prooning.BreathFirst_P(instance)
            cProfile.run('bfp.run()')
            # result = bfp.run()

            print(result[0])
            print(result[1])
