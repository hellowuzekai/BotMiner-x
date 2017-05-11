import numpy as np
from sklearn.cluster import AffinityPropagation
import csv
import os

def  affinityPropagation(p1,p2):
    ip_src = []
    ip = open("ip.csv", "r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    print len(ip_src)
    result = []

    X = np.loadtxt("tmp.csv", delimiter=",", skiprows=0, ndmin=2)
    ap = AffinityPropagation(preference=p1,damping=p2).fit(X)
    cluster_centers_indices = ap.cluster_centers_indices_
    labels = ap.labels_

    n_clusters_ = len(cluster_centers_indices)
    print('num:%d' % n_clusters_)
    affinityprogation = [[] for c in range(n_clusters_)]
    print('Estimated number of clusters: %d' % n_clusters_)

    for i in xrange(len(labels)):
        affinityprogation[labels[i]].append(ip_src[i])
    for i in range(n_clusters_):
        print len(affinityprogation[i]), affinityprogation[i]
        result.append((affinityprogation[i]))
    csvfile = file(os.getcwd() + "/result/affinity/" + str(p1) + '--' + str(p2) + " clusters=" + str(n_clusters_) + '.csv',
                   'ab+')
    writer = csv.writer(csvfile)
    writer.writerows(result)
    csvfile.close()