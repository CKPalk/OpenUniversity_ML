
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


	TrainDF = pd.read_csv( csv_filename )


	# Create data subset
	TrainDF = TrainDF[ TrainDF.Year > 2008 ]
	TrainDF['Week'] = TrainDF['Dates'].map( lambda x: 
		time.strftime( "%U", time.strptime(x, '%Y-%m-%d %H:%M:%S' ) ) )
	TrainDF['event'] = 1

	weekly_events = TrainDF[['Week', 'Year', 'event' ]].groupby(['Year','Week']).count().reset_index()
	weekly_events_year = weekly_events.pivot( index='Week',
			columns='Year', values='event' )
	
	ax = weekly_events_year.interpolate().plot( title='Cases per week', 
			figsize=(10,6))

	# Plot setup


	plt.savefig( output_filename )

	print( "Figure saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

