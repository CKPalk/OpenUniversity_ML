import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys

plt.style.use('ggplot')


# We can first visualize the distribution of crimes over a day (by hours) in different months:
import re
def parse_date(date):
	mo=re.search(r'^([0-9]{4})-([0-9]{2})-[0-9]{2}\s+([0-9]{2}):[0-9]{2}:[0-9]{2}$',date)
	return map(int,(mo.group(1),mo.group(2),mo.group(3)))
# Extract 'Year', 'Month' and 'Hour' columns for later use
month_dict={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

train_data = pd.read_csv( sys.argv[ 1 ], parse_dates=['Dates'], date_parser=lambda x: 
		pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S' ) )

train_data['Hour'] = train_data.Dates.map( lambda x: x.hour )

data_month_hour=pd.crosstab(train_data.Hour,train_data.Month)
axhandles=data_month_hour.plot(kind='bar',subplots=True,layout=(4,3),figsize=(16,12),sharex=True,sharey=True,xticks=range(0,24,4),rot=0)
# Note here the subplots are based on columns, each column a new subplot
i=1
for axrow in axhandles:
	for ax in axrow:
		ax.set_xticklabels([ str(i) if i % 4 == 0 else '' for i in range(24) ] )
		ax.legend([month_dict[i]],loc='best')
		# Note here the argument has to be a list or a tuple, e.g. (month_dict[i],).
		# From Matplotlib official documentation: To make a legend for lines which already exist on the axes (via plot for instance),
		#    simply call this function with an ITERABLE of strings, one for each legend item.
		ax.set_title("")
		i+=1
plt.suptitle('Distribution of Crimes by Hour',size=20)
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.savefig('Distribution_of_Crimes_by_Hour.png')
