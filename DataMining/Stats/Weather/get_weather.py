import sys
import json
import os
import seaborn as sb
import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib.request import Request



key = '7ad6e966485527aa'


def getWeatherJSON( day, month, year ):
	url = "http://api.wunderground.com/api/{key}/history_{YYYY}{MM:0>2d}{DD:0>2d}/q/OR/Eugene.json".format(
		key	= key,
		YYYY = year,
		MM = month,
		DD = day )
	request = Request( url )
	with urlopen( request ) as response:
		response = response.read()
	parsed_json = json.loads( response.decode('utf-8') )
	return parsed_json



def saveWeatherForDates( dates, filename ):
	data = {}
	for date in dates:
		print( "Getting weather for", date.strftime( '%Y-%m-%d' ) )
		data[ date.strftime( '%Y-%m-%d' ) ] = getWeatherJSON( date.day, date.month, date.year )
	with open( filename, 'w+' ) as stream:
		stream.write( json.dumps( data ) )
	print( "Written json dump to", filename )
	return



def getUniqueDates( csv_filename ):
	df = pd.read_csv( csv_filename, parse_dates=['Dates'], date_parser=lambda
			x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )
	return ( df[ 'Dates' ].map( pd.Timestamp.date ).unique() )


def main( argv ):
	unique_dates = getUniqueDates( argv[1] )
	saveWeatherForDates( unique_dates, argv[2] )

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



