import numpy as np
def createboard(filename):
    dimension=int(filename[-7]) 																		#definieer dimensie op basis van bestandsnaam
    boarddummy=np.zeros((dimension+2,dimension+2), int).astype(str) 									#Creeer een array met nullen op basis van dimensie om vol te zetten met auto's

    boarddummy[0]='|'																					#eerste rij van muren voorzien
    boarddummy[-1]='|'																					#laatste rij van muren voorzien

    for x in boarddummy:	
        x[0]='|'																						#eerste kolom van muren voorzien
        x[-1]='|'																						#laatste kolom van muren voorzien

    boarddummy[(len(boarddummy)-int(len(boarddummy)/2)-1)][-1]='.'										#creer poortje aangegeven met '.'
    return boarddummy


def populateboard(cars,basis):																		    #Functie om het dummy bord op basis van de input van auto's te voorzien
	board=basis
	for row in cars.itertuples():																    #loop door input dataframe
		posx= 7-row.col
		posy= row.row
		board[posx][posy]=board[posx][posy].replace('0',row.car)						    #Vervang 0 met de relevante auto letter
		if row.orientation=='H':																	    #check of de auto horizontaal of verticaal is georienteerd om te bepalen waar de volgende letter moet komen
			board[posx][posy+1]=board[posx][posy+1].replace('0',row.car)
			if row.length==3:																		    #check hoe groot de auto is om te bepalen of er nog een derde letter bij moet komen
				board[posx][posy+2]=board[posx][posy+2].replace('0',row.car)
		if row.orientation=='V':
			board[posx-1][posy]=board[posx-1][posy].replace('0',row.car)
			if row.length==3:
				board[posx-2][posy]=board[posx-2][posy].replace('0',row.car)
	return board
