# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np
import csv
from sklearn import metrics
ip_src = []
ip = open("ip.csv", "r")
ip_src = ip.read().split("\n")[:-1]
ip.close()
print len(ip_src)
csvfile = file('result.csv', 'ab+')
writer = csv.writer(csvfile)
result=[]
X = np.loadtxt("tmp.csv", delimiter=",", skiprows=0, ndmin=2)
# plt.scatter(X[:, 0], X[:, 1], marker='*', c='r',s = 1)
# plt.show()
n=55
k_means = KMeans(init="k-means++",n_clusters=n,n_init=10)
y_pred = k_means.fit_predict(X)
print y_pred
kmeans = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for i in xrange(len(y_pred)):
    kmeans[y_pred[i]].append(ip_src[i])
for i in range(n):
    print len(kmeans[i]), kmeans[i]
    result.append((kmeans[i]))
writer.writerows(result)
csvfile.close()

print 'Calinski-Harabasz Score', metrics.calinski_harabaz_score(X, y_pred)
# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].


