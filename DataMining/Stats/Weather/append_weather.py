
from urllib.request import urlopen
from urllib.request import Request
import json
import sys
import pandas as pd
import numpy as np


date_format = '%Y-%m-%d'
datetime_format = date_format + ' %H:%M:%S'


def appendAttrsIfNeeded( df ):
	if 'Temp' not in df.columns:
		df['Temp'] = np.nan
	if 'Rain' not in df.columns:
		df['Rain'] = np.nan
	return df


def findTempAndRain( json, date ):
	date_str = date.strftime( date_format )

	try:
		loc1 = json[date_str]
		loc2 = loc1['history']
		loc3 = loc2['observations']
		observation = loc3[ date.hour - 1]
		temperature = float( observation[ 'tempi' ] )
		rain = int( observation[ 'rain' ] )
		return ( temperature, rain )
	except:
		return ( np.nan, np.nan )



def addWeatherData( json_filename, csv_filename ):

	js = json.loads( open( json_filename, 'r' ).read() )
	df = pd.read_csv( csv_filename, parse_dates=['Dates'], date_parser=lambda
			x: pd.datetime.strptime(x, datetime_format ) )

	df = appendAttrsIfNeeded( df )

	for idx, row in df.iterrows():
		if pd.isnull( row['Temp'] ) and pd.isnull( row['Rain'] ):
			temp_rain = findTempAndRain( js, row['Dates'] )
			print( "Setting temperature {} and rain {} for row {}".format( str(temp_rain[0]), str(temp_rain[1]), str(idx) ) )
			df.set_value( idx, 'Temp', temp_rain[0] )
			df.set_value( idx, 'Rain', temp_rain[1] )
		else:
			print( "Found temperature", row['Temp'] )
			print( "Found rain", row['Rain'] )
			print()

	df.to_csv( csv_filename, index=False )

	print( "File saved" )






	#response = getWeatherJSON( 9, 6, 1994 )
	#print( response['history']['dailysummary'][0]['meantempi'] )

def main( argv ):
	addWeatherData( argv[1], argv[2] )


if __name__ == '__main__':
	main( sys.argv )

