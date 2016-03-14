
from urllib.request import urlopen
from urllib.request import Request
import json
import sys
import pandas as pd
import numpy as np

key = '7ad6e966485527aa'

def getWeatherJSON( day, month, year ):

	url = "http://api.wunderground.com/api/{key}/history_{YYYY}{MM:0>2d}{DD:0>2d}/q/OR/Eugene.json".format(
		key	 = key,
		YYYY = year,
		MM	 = month,
		DD	 = day )

	request = Request( url )
	with urlopen( request ) as response:
		response = response.read()
	parsed_json = json.loads( response.decode('utf-8') )
	return parsed_json


def appendAttrsIfNeeded( df ):
	if 'Temp' not in df.columns:
		df['Temp'] = np.nan
	if 'Rain' not in df.columns:
		df['Rain'] = np.nan
	return df


def findTempAndRain( date ):
	json = getWeatherJSON( date.day, date.month, date.year )

	observation = json['history']['observations'][date.hour - 1]

	temperature = float( observation[ 'tempi' ] )
	if temperature < -50:
		temperature = None
	
	rain = int( observation[ 'rain' ] )

	return ( temperature, rain )

	



	temperature = json['history']['observations'][date.hour - 1]['tempi']

	



def addWeatherData( csv_filename ):

	df = pd.read_csv( csv_filename, parse_dates=['Dates'], date_parser=lambda
			x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )

	df = appendAttrsIfNeeded( df )

	for idx, row in df.iterrows():
		if pd.isnull( row['Temp'] ) and pd.isnull( row['Rain'] ):
			temp_rain = findTempAndRain( row['Dates'] )
			print( "Setting temperature and rain for row", idx )
			df.set_value( idx, 'Temp', temp_rain[0] )
			df.set_value( idx, 'Rain', int( temp_rain[1] ) )
			break
		else:
			print( "Found temperature", row['Temp'] )
			print( "Found rain", row['Rain'] )
			print()

	df.to_csv( csv_filename, index=False )

	print( "File saved" )






	#response = getWeatherJSON( 9, 6, 1994 )
	#print( response['history']['dailysummary'][0]['meantempi'] )

def main( argv ):
	addWeatherData( argv[1] )


if __name__ == '__main__':
	main( sys.argv )

