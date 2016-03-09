''' Work of Cameron Palk '''

import sys
import pandas as pd

def main( argv ):
	try:
		csv_filepath 	= argv[ 0 ]
		output_filepath = argv[ 1 ]
	except IndexError:
		print( "Error, usage: \"python3 coord_bounds.py <CSV> <output_file>\"" ) 
		return
	
	training_data = pd.read_csv( csv_filepath )

	training_data[ 'clean_Latitude'  ] = training_data[ training_data.Latitude   > 47  ].Latitude
	training_data[ 'clean_Longitude' ] = training_data[ training_data.Longitude < -122 ].Longitude

	training_data.dropna()

	print( training_data[ 'clean_Latitude' ] )

	for axis in [ 'clean_Longitude', 'clean_Latitude' ]:
		print( "{:16}   min: {:16}   max: {:16}".format( 
			axis,
			min( training_data[ axis ] ), 
			max( training_data[ axis ] ) 
		) )

	#

if __name__=='__main__':
	main( sys.argv[ 1: ] )
