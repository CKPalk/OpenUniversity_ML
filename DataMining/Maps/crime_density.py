
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sb
import sys



# Map bounding box 
mapbox_lon_min = -122.4797
mapbox_lon_max = -122.2050

mapbox_lat_min =   47.4671
mapbox_lat_max =   47.7476

# used in kernel density estimate plot
mapbox   = (   -122.4797, -122.2050,     47.4671, 47.7476   )
clipsize = [ [ -122.4797, -122.2050 ], [ 47.4671, 47.7476 ] ]


def main( argv ):
	try:
		program_name 	= argv[ 0 ]
		csv_filename 	= argv[ 1 ]
		map_filename	= argv[ 2 ]
		output_filename = argv[ 3 ]
	except TypeError:
		print( "Usage: 'python3 {} <csv_file> <map_file> <output_file>'".format( sys.argv[0] ) )
		return

	# Init map
	mapdata = np.loadtxt( map_filename )
	asp = mapdata.shape[0] * 1.0 / mapdata.shape[1]


	train = pd.read_csv( csv_filename )

	# Filter the lat/longs not in our maps range
	train[ 'clean_Latitude'  ] = train[ train.Latitude  > mapbox_lat_min ].Latitude
	train[ 'clean_Longitude' ] = train[ train.Longitude < mapbox_lon_max ].Longitude
	train.dropna()
	
	trainB = train[ train.Summarized_Offense_Description == 'BURGLARY' ]

	# Plot setup
	pl.figure( figsize = ( 20, 20 * asp ) )
	ax = sns.kdeplot( trainB.clean_Latitude, trainB.clean_Longitude, clip=clipsize, aspect=1/asp )
	ax.imshow( mapdata, cmap=pl.get_cmap('gray'),
				extend=mapbox,
				aspect=asp )
	
	pl.savefig( 'burglary_density_plot.png' )

	#

if __name__=='__main__':
	main( sys.argv )

