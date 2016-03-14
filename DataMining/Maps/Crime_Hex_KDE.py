
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sb
import sys

from scipy import stats



# Map bounding box 
mapbox_lon_min = -122.4797
mapbox_lon_max = -122.2050

mapbox_lat_min =   47.4671
mapbox_lat_max =   47.7476

# used in kernel density estimate plot
mapbox   = (   -122.4797, -122.2050,	 47.4671, 47.7476   )
clipsize = [ [ -122.4797, -122.2050 ], [ 47.4671, 47.7476 ] ]

map_size_inches = 10


def main( argv ):
	try:
		program_name	= argv[ 0 ]
		csv_filename	= argv[ 1 ]
		map_filename	= argv[ 2 ]
		output_filename = argv[ 3 ]
	except:
		print( "Usage: 'python3 {} <csv_file> <map_file> <output_file>'".format( sys.argv[0] ) )
		return

	# Init map
	mapdata = mpimg.imread( map_filename )
	asp = mapdata.shape[0] * 1.0 / mapdata.shape[1]


	TrainDF = pd.read_csv( csv_filename )
	TrainDF = TrainDF[1:10000]


	''' Create a training data subset to map '''

	TrainDF.dropna()


	# Plot setup
	plt.figure( 
		figsize = ( map_size_inches, map_size_inches * asp ) 
	)

	print( "Building swarm plot" )
	ax = sb.swarmplot( x = 'Month', y = 'Summarized_Offense_Description', data = TrainDF )


	plt.savefig( output_filename )

	print( "Plot image saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

