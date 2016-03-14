
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

	Data[ 'Date' ] = Data[ 'Occurred_Date_or_Date_Range_Start' ].map( lambda x:
			time.strptime( x, '%m/%d/%y %H:%M' ) )

	Data[ 'Dates' ] = Data[ 'Date' ].map( lambda x:
			time.strftime( '%Y-%m-%d %H:%M:%S', x ) )

	Data[ 'Summary' ] = Data[ 'Summarized_Offense_Description' ].map( id )

	Data[ 'Lon' ] = Data[ 'Longitude' ].map( id )

	Data[ 'Lat' ] = Data[ 'Latitude' ].map( id )

	Data[ 'Day_num' ] = Data[ 'Date' ].map( lambda x: 
			x.tm_wday + 1 )

	Data[ 'Day_str' ] = Data[ 'Day_num' ].map( lambda x:
			{ 1 : 'Monday',
			  2 : 'Tuesday',
			  3 : 'Wednesday',
			  4 : 'Thursday',
			  5 : 'Friday',
			  6 : 'Saturday',
			  7 : 'Sunday ' }[ x ] )

	Data[ 'Day_num' ] = Data[ 'Date' ].map( lambda x: 
			x.tm_wday + 1 )


	Data.drop( [ 
		'Date',
		'Longitude',
		'Latitude',
		'Summarized_Offense_Description',
		'Occurred_Date_or_Date_Range_Start', 
		'RMS_CDW_ID', 
		'General_Offense_Number', 
		'Offense_Code',
		'Summary_Offense_Code',
		'Offense_Type',
		'Offense_Code_Extension'
	], axis=1, inplace=True )


	Data = Data[ [ 
		'District',
		'Zone',
		'Dates',
		'Day_str',
		'Day_num',
		'Month',
		'Year',
		'Summary',
		'Lon',
		'Lat' 
	] ]


	for a in Data.Summary.unique():
		print(a)


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

