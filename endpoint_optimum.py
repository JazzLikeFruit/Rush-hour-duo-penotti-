from code.algorithms import random_algorithm, unique_moves, short_path, end_point, breadth_first, breadthfirst_prooning
from code.classes import cars, board
from numpy import random
import csv
import time
import plotly.express as px
import pandas as pd

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

    iterations = []
    times = []
    results = []
    algo = []
    resultdic = {}
    start = time.time()

    print(f"Board {game} chosen")
    instance = board.Board(datafile)
    empty_board = instance.create_board()
    cardic = instance.load_cars(datafile)

    threshold = 0

    while threshold <= 1:
        ep = end_point.End_point(instance, cardic)
        
        while len(iterations) < 6:
            startiteration = time.time()
            result = ep.random_run(threshold)
            times.append(time.time()-startiteration)
            results.append(result[0])
            algo.append('Random')
            iterations.append(len(iterations)+1)

        threshold += 0.1

    resultdic['Iteration'] = iterations
    resultdic['Time'] = times
    resultdic['Movements'] = results
    resultdic['Algorithm'] = algo
    df = pd.DataFrame.from_dict(resultdic)
    df['Avg Move'] = df.groupby('Algorithm')['Movements'].transform(
        'mean').round().astype(int)
    df['Avg Time'] = df.groupby('Algorithm')[
        'Time'].transform('mean').round(2)
    print(df)
    fig = px.histogram(df[['Movements', 'Algorithm']],
                        x="Algorithm", y="Movements", histfunc="avg")
    fig.show()
    fig = px.histogram(df[['Time', 'Algorithm']],
                        x="Algorithm", y="Time", histfunc="avg")
    fig.show()


