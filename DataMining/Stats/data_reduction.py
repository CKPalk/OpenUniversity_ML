
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sb
import sys
import time

from scipy import stats


def id( x ):
	return x

def cleanCSV( csv_in, csv_out ):

	Data = pd.read_csv( csv_in )

	dontWant = [ 
		'OTHER PROPERTY',
		'LOST PROPERTY',
		'THEFT OF SERVICES', 
		'[INC - CASE DC USE ONLY]',
		'RECOVERED PROPERTY',
		'FRAUD', 
		'FORGERY', 
		'EMBEZZLE',
		'ELUDING',
		'BIAS INCIDENT', 
		'FALSE REPORT',
		'PUBLIC NUISANCE',
		'EXTORTION', 
		'OBSTRUCT',
		'STAY OUT OF AREA OF DRUGS', 
		'PURSE SNATCH',
		'FIREWORK', 
		'ESCAPE',
		'PORNOGRAPHY', 
		'GAMBLE',
		'STAY OUT OF AREA OF PROSTITUTION', 
		'HARBOR CALLs',
		'HARBOR CALLS', 
		'Purse Snatch' ,
		'Car Prowl',
		'RECKLESS BURNING',
		'Shoplifting',
		'LOITERING',
		'DISORDERLY CONDUCT',
		'Bike Theft',
		'ILLEGAL DUMPING'
	]

	Data.Summary = Data.Summary.map( lambda x: 
		( np.nan if x in dontWant else x ))

	Data.dropna( subset=['Summary'], inplace=True)

	Data.to_csv( csv_out, index=False )


def main( argv ):
	try:
		program_name	= argv[ 0 ]
		csv_in			= argv[ 1 ]
		csv_out 	 	= argv[ 2 ]
	except:
		print( "Usage: 'python3 {} <csv_file> <map_file> <output_file>'".format( sys.argv[0] ) )
		return

	cleanCSV( csv_in, csv_out )


if __name__=='__main__':
	main( sys.argv )

