
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from contextlib import contextmanager

import sys
import operator
import string
import codecs
import io
import os


def plot_bar( df, title, filename ):
	p = (
		'Set2', 'Paired', 'colorblind', 'husl',
		'Set1', 'coolwarm', 'RdYlGn', 'spectral'
	)
	color = sns.color_palette(np.random.choice(p), len(df))
	bar = df.plot( kind = 'barh',
			title = title,
			fontsize = 8,
			figsize=(12,8),
			stacked = False,
			width = 1,
			color = color
	)
	bar.figure.savefig( filename )

	plt.show()

def plot_years( df, column, title, fname, items=0):
	lower_case     = operator.methodcaller('lower')
	df.columns     = df.columns.map(lower_case)

	df.year = df[ df.year > 2007 ].year

	by_col         = df.groupby( [column] )
	col_freq       = by_col.size()

	col_freq.sort_values(ascending=True, inplace=True)

	plot_bar( title, fname )


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
	plot_years( TrainDF, 'year', 'Top Crime Categories', output_filename )


	print( "Figure saved successfully as", output_filename )
	return
#


if __name__=='__main__':
	main( sys.argv )

