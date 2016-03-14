
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sb
import sys




def main( argv ):
	try:
		program_name	= argv[ 0 ]
		csv_filename	= argv[ 1 ]
		output_filename = argv[ 2 ]
	except:
		print( "Usage: 'python3 {} <csv_file> <output_file>'".format( sys.argv[0] ) )
		return


	TrainDF = pd.read_csv( csv_filename )


	# Create data subset
	TrainDF = TrainDF[ TrainDF.Year == 2015 ]
	TrainDF = TrainDF[ TrainDF.Summary == 'BURGLARY' ]

	TrainDF.dropna()

	# Plot setup


	plt.savefig( output_filename )

	print( "Figure saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

