
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl
import seaborn as sb
import sys

import time


def main( argv ):
	try:
		program_name	= argv[ 0 ]
		csv_filename	= argv[ 1 ]
		output_filename = argv[ 2 ]
	except:
		print( "Usage: 'python3 {} <csv_file> <output_file>'".format( sys.argv[0] ) )
		return


	df = pd.read_csv( csv_filename )
	df.dropna( inplace=True )
	# Create data subset
	df['event'] = 1
	df.Temp = df[ df.Temp > 0 ].Temp
	df.Temp = df.Temp.map( round )

	# Plot setup
	plt.style.use('ggplot')


	temp_event = pd.crosstab( df.Temp, df.event )
	ax = temp_event.plot( kind='bar', figsize=(16,12), rot=0 )

	plt.suptitle('Distribution of Crimes by Hour',size=20)
	plt.tight_layout()

	plt.savefig( output_filename )
	plt.show()

	print( "Figure saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

