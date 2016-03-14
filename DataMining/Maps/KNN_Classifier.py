
import pandas as pd
import numpy as np
import math
import zipfile
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

import sys

def llfun(act, pred):
	""" Logloss function for 1/0 probability """
	return (-(~(act == pred)).astype(int) * math.log(1e-15)).sum() / len(act)


train = pd.read_csv( sys.argv[ 1 ], parse_dates=['Dates'])


# Separate test and train set out of orignal train set.
msk = np.random.rand(len(train)) < 0.8
knn_train = train[msk]
knn_test = train[~msk]
n = len(knn_test)

print("Original size: %s" % len(train))
print("Train set: %s" % len(knn_train))
print("Test set: %s" % len(knn_test))

# Prepare data sets
#x = knn_train[[ 'Day_num', 'Month', 'Year', 'Lon', 'Lat']]
x = knn_train[[ 'Lon', 'Lat']]
y = knn_train['Summary'].astype('category')
actual = knn_test['Summary'].astype('category')


# Fit
logloss = []
for i in range(1, 50, 1):
	knn = KNeighborsClassifier(n_neighbors=i)
	knn.fit(x, y)
						    
	# Predict on test set
	#outcome = knn.predict(knn_test[[ 'Day_num', 'Month', 'Year', 'Lon', 'Lat']])
	outcome = knn.predict(knn_test[[ 'Lon', 'Lat']])
									    
	# Logloss
	logloss.append(llfun(actual, outcome))

plt.plot(logloss)
plt.savefig('n_neighbors_vs_logloss.png')

# Submit for K=40
if len( sys.argv ) != 3: sys.exit( 0 )

test = pd.read_csv( sys.argv[ 2 ], parse_dates=['Dates'])
x_test = test[['District', 'Zone', 'Day_num', 'Month', 'Year', 'Lon', 'Lat']]
knn = KNeighborsClassifier(n_neighbors=40)
knn.fit(x, y)
outcomes = knn.predict(x_test)

submit = pd.DataFrame({'Id': test.Id.tolist()})
for category in y.cat.categories:
	submit[category] = np.where(outcomes == category, 1, 0)
														    
submit.to_csv('k_nearest_neigbour.csv', index = False)
