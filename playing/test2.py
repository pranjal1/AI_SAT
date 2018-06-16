import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets, svm



iris = datasets.load_iris()
X = iris["data"]
Y = iris["target"]
feature_names = iris["feature_names"]

print "the shape of X is : ",X.shape
print "the shape of Y is : ",Y.shape
print "the features are:"

for i in feature_names:
	print ' '*4,i

df = pd.DataFrame(X)
df.head()

df.columns = feature_names
df.head()

df["iris_type"] = Y
df.head()

df.plot(figsize=(11, 11))
plt.show()



plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Set1,
            edgecolor='k')

#above line is simple to understand
#(X[:, 0], X[:, 1]) means (sepal length, sepal width)
#c=Y means color will be (0,1,2) depending on the flower type for the (sepal length, sepal width) i.e Y
#cmap selects one from different coloring scheme are present
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Iris data 2D')
plt.show()




fig = plt.figure(figsize=(8, 6))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(X[:, 0], X[:, 1], X[:, 2],
               c=Y.astype(np.float), edgecolor='k')
ax.set_xlabel(feature_names[0])
ax.set_ylabel(feature_names[1])
ax.set_zlabel(feature_names[2])
plt.show()



kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)
Y_pred = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=Y_pred, cmap=plt.cm.Set1, edgecolor='k')
plt.show()
