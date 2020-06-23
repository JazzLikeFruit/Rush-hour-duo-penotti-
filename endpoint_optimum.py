from code.algorithms import end_point
from code.classes import cars, board
import numpy as np
import csv
import plotly.express as px
import pandas as pd
import copy

if __name__ == '__main__':
    print("\nEND POINT OPTIMUM TESTER - Duo Penotti\n")

    # Get user input for testing variables
    thresholdstart = float(input("threshold min?\ninput number between 0-0.8\n"))
    thresholdend = float(input("\nthreshold max?\ninput number < 1\n"))
    maxiterations = int(input("\nhow many repetitions per run?\n"))

    # Set bigthreshold values
    bigthresholdstart = thresholdstart * 10
    bigthresholdend = thresholdend * 10
    
    thresholdlist = []
    resultlist = []
    datafilelist = []
    maxiterationslist = []

    # Make dictionary to save results per threshold iteration to calculate mean
    results = {}
    #avgresult = {}

    bigthreshold = bigthresholdstart

    iteration = 0
    files = ["data/Rushhour6x6_1.csv", "data/Rushhour6x6_2.csv", "data/Rushhour6x6_3.csv", "data/Rushhour9x9_4.csv", "data/Rushhour9x9_5.csv", "data/Rushhour9x9_6.csv"]
    
    print("starting run...")
    # Make instance for every board file
    for boardfile in files[:-1]:

        datafile = boardfile
        instance = board.Board(datafile)
        cardic = instance.load_cars(datafile)

        empty_board = instance.create_board()
        print(instance.load_board(empty_board))

        ep = end_point.End_point(instance, cardic)

        resultdic={"Threshold":[], "AVG":[], "Board":[], "Repetitions":[]}

        print(f"busy with board {datafile}")

        # increment threshold / bigthreshold with 0.1 / 1
        while bigthreshold < bigthresholdend:
            threshold = bigthreshold / 10
            results[threshold] = []
            iteration = 0

            # Repeat the algorithm a specified amount of times
            while iteration < maxiterations:
                
                # Run the algorithm
                result = ep.random_run(threshold)[0]
                results[threshold].append(result)

                # Reload the board
                instancecopy = copy.deepcopy(instance)
                cardic = instancecopy.load_cars(datafile)
                empty_board = instancecopy.create_board()
                instancecopy.load_board(empty_board)

                ep = end_point.End_point(instancecopy, cardic)

                iteration += 1
                
            # Save data for figure
            thresholdlist.append(threshold)
            datafilelist.append(datafile)
            maxiterationslist.append(maxiterations)
            
            # Calculate mean
            resultlist.append(np.mean(results[threshold]))

            bigthreshold += 1
        
        bigthreshold = bigthresholdstart

    # Add data to resultdic
    resultdic["Threshold"]=thresholdlist
    resultdic["Average Movement"]=resultlist
    resultdic["Board"]=datafilelist
    resultdic["Repetitions"] = maxiterationslist

    # Create figures
    dfend=pd.DataFrame.from_dict(resultdic)
    dfend.to_csv("dfendoutput.csv")
    fig = px.line(dfend,
                    x="Threshold", y="Average Movement",  facet_col="Board", facet_col_wrap=3)
    fig.show()


        