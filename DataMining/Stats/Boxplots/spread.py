
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

df = pd.read_csv( sys.argv[ 1 ] )

plt.boxplot( df[ ( df.Lon < -100 ) & ( df.Lon > -125 ) ].Lon )
axes = plt.gca()
#axes.set_ylim( -123, -122 )
plt.show() 
