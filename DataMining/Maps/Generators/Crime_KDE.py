
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


	''' Create a training data subset to map 
	District, Zone, Dates, Day_str, Day_num, Month, Year, Summary, Lon, Lat
	'''

	TrainDF = TrainDF[ TrainDF.Year == 2015 ]
	TrainDF = TrainDF[ TrainDF.Summary == 'BURGLARY' ]

	TrainDF[ 'Xok' ] = TrainDF[ TrainDF.Lon < mapbox_lon_max ].Lon
	TrainDF[ 'Yok' ] = TrainDF[ TrainDF.Lat > mapbox_lat_min ].Lat

	TrainDF.dropna()


	# Create data subset

	# Plot setup
	plt.figure( 
		figsize = ( map_size_inches, map_size_inches * asp ) 
	)

	print( "Building Kernel Density Estimate Plot" )
	ax = sb.kdeplot( TrainDF.Xok, TrainDF.Yok, 
		clip 	= clipsize, 
		aspect 	= 1 / asp
	)

	# Show map
	ax.imshow( mapdata, 
		cmap	= plt.get_cmap('gray'), 
		extent	= mapbox,
		aspect 	= asp
	)

	plt.savefig( output_filename )

	print( "Plot image saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

