
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sb
import sys



# Map bounding box 
mapbox_lon_min = -122.4797
mapbox_lon_max = -122.2050

mapbox_lat_min =   47.4671
mapbox_lat_max =   47.7476

# used in kernel density estimate plot
mapbox   = (   -122.4797, -122.2050,	 47.4671, 47.7476   )
clipsize = [ [ -122.4797, -122.2050 ], [ 47.4671, 47.7476 ] ]


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

	train = pd.read_csv( csv_filename )

	# Filter the lat/longs not in our maps range
	train[ 'clean_Latitude'  ] = train[ train.Latitude  > mapbox_lat_min ].Latitude
	train[ 'clean_Longitude' ] = train[ train.Longitude < mapbox_lon_max ].Longitude
	train.dropna()

	print( min( train['clean_Latitude'] ) )
	print( max( train['clean_Latitude'] ) )

	print( min( train['clean_Longitude'] ) )
	print( max( train['clean_Longitude'] ) )

	print( train.columns )
	trainB = train[ train.SOC == 'BURGLARY' ]

	# Plot setup
	#f, ax = plt.figure( figsize = ( 20, 20 * asp ) )
	#plt.imshow( mapdata )
	#sb.kdeplot( trainB.clean_Longitude, trainB.clean_Latitude, ax=ax )
	#plt.imshow( mapdata, cmap=plt.get_cmap('gray'), extend=mapbox, aspect=asp )

	data = np.random.multivariate_normal([0,0],[[1,2],[2,20]], size=1000)
	data = pd.DataFrame(data, columns=["X","Y"])
	mpl.rc("figure", figsize=(6,6))
	print( trainB.clean_Longitude )
	print( trainB.clean_Latitude )
	sb.kdeplot( trainB.clean_Longitude, trainB.clean_Latitude )

	plt.savefig( 'burglary_density_plot.png' )

	#

if __name__=='__main__':
	main( sys.argv )

