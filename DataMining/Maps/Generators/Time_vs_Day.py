

#
# Preparing the data
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

df = pd.read_csv( sys.argv[ 1 ] )

# Add column containing day of week expressed in integer

df[ 'DOW' ] = df.Day_num.map( lambda x: x-1 )

# Add column containing time of day
df[ 'Hour' ] = pd.to_datetime(df.Dates).dt.hour

# Retrieve categories list
cats = pd.Series(df.Summary.values.ravel()).unique()
cats.sort()

plt.figure(1,figsize=(6,5))
plt.hist2d( 
	df.Hour.values,
	df.DOW.values,
	bins=[24,7],
	range=[[-0.5,23.5],[-0.5,6.5]]
)

plt.suptitle( "All Crime ( DOW vs. Time )" )
plt.xticks(np.arange(0,24,6))
plt.xlabel('Time of Day')
plt.yticks(np.arange(0,7),['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
plt.ylabel('Day of Week')
plt.xticks(np.arange(0,24), [ 
	'12AM', '', 
	'2AM', '', 
	'4AM', '', 
	'6AM', '', 
	'8AM', '', 
	'10AM', '', 
	'12PM', '', 
	'2PM', '', 
	'4PM','',
	'6PM', '', 
	'8PM', '', 
	'10PM', '' ], rotation=270 )

plt.gca().invert_yaxis()

plt.savefig( sys.argv[ 2 ] )
