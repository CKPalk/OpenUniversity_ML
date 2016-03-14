
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


	''' Create a training data subset to map '''

	TrainDF[ 'Xok' ] = TrainDF[ TrainDF.Lon < mapbox_lon_max ].Lon
	TrainDF[ 'Yok' ] = TrainDF[ TrainDF.Lat > mapbox_lat_min ].Lat

	TrainDF.dropna()

	TrainDF = TrainDF[1:30000]


	# Plot setup
	g = sb.FacetGrid( TrainDF,
		col = 'Summary',
		col_wrap = 5,
		size = 5,
		aspect = 1 / asp
	)

	sb.set_style( "whitegrid" )

	for ax in g.axes:
		ax.grid( False )
		ax.imshow( mapdata, 
			cmap	= plt.get_cmap('gray'), 
			extent	= mapbox,
			aspect 	= asp
		)
	
	g.set(xticks=[])
	g.set(yticks=[])

	
	g.map( sb.kdeplot, 'Xok', 'Yok', clip=clipsize )
	g.set_titles( col_template="{col_name}", fontweight='bold' )

	# plt.suptitle( 'Kernel Density Estimation Plots' )

	plt.savefig( output_filename )

	print( "Plot image saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

