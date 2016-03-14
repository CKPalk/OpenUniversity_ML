import sys
import json
import os
import seaborn as sb
import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib.request import Request


def getUniqueDates( csv_filename ):
	df = pd.read_csv( csv_filename, parse_dates=['Dates'], date_parser=lambda
			x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )
	return ( df[ 'Dates' ].map( pd.Timestamp.date ).unique() )


def main( argv ):
	unique_dates = getUniqueDates( argv[1] )
	print( len( unique_dates ) )

if __name__ == '__main__':
	main( sys.argv )




def findTempAndRain( date ):
	json = getWeatherJSON( date.day, date.month, date.year )

	observation = json['history']['observations'][date.hour - 1]

	temperature = float( observation[ 'tempi' ] )
	if temperature < -50:
		temperature = None

	rain = int( observation[ 'rain' ] )

	return ( temperature, rain )



