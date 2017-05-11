import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
import  os
def tdbScan(p1,p2):
    result = []
    ip_src = []

    ip = open("ip.csv", "r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    print len(ip_src)
    X = np.loadtxt("tmp.csv", delimiter=",", ndmin=0)
    db = DBSCAN(eps=p1, min_samples=p2).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_


    # dbscan=[]
    print len(set(labels))
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print n_clusters_
    dbscan = [[] for c in range(n_clusters_)]
    print('clusters: %d' % n_clusters_)

    for i in xrange(len(labels)):
        dbscan[labels[i]].append(ip_src[i])
    for i in range(n_clusters_):
        result.append((dbscan[i]))
    if os.path.isfile(os.getcwd()+"/result.csv"):
        os.remove(os.getcwd()+"/result.csv")
    csvfile = file(os.getcwd() + "/result/tbscan/"+str(p1) + '--' + str(p2) +" clusters="+ str(n_clusters_)+'.csv', 'ab+')
    writer = csv.writer(csvfile)
    writer.writerows(result)
    csvfile.close()



