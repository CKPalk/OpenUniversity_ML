
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


	orig = pd.read_csv( sys.argv[ 1 ], parse_dates=['Dates'], date_parser=lambda x: 
			pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ).date() )

	orig.Temp = orig[ orig.Temp > -50 ].Temp
	orig.Temp = orig.Temp.map( round )
	# Add a count column
	orig[ 'Count' ] = 1
	orig.dropna( inplace=True )

	temperatures = orig.Temp.unique()

	dat_df = orig[[ 'Dates', 'Temp' ]].copy()
	dat = dat_df.groupby( 'Dates', as_index=False ).Temp.mean()

	cat_df = orig[[ 'Dates', 'Temp' ]].copy()
	cat_df.Temp = cat_df.Temp.map( lambda x: 

	days_at_temp = { t:len( orig[ orig.Temp == t ] ) for t in temperatures }

	#print( days_at_temp )

	#crimes_at_temp 	= cat_df.groupby( 'Temp' ).count()
	#days_at_temp 	= dat_df.groupby( 'Temp' ).count()

	print( dat )





	# Plot setup
	plt.style.use('ggplot')

	#temp_event = pd.crosstab( df.Temp, df.event )


	#ax = temp_event.plot( kind='bar', figsize=(16,12), rot=0 )

	#plt.suptitle('Distribution of Crimes by Hour',size=20)
	#plt.tight_layout()

	#plt.savefig( output_filename )
	#plt.show()

	print( "Figure saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

