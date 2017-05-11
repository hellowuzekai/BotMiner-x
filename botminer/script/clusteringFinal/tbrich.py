# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import Birch
import csv
from sklearn import metrics
import os

def tbrich(p1,p2):
        ip_src = []
        ip = open("ip.csv", "r")
        ip_src = ip.read().split("\n")[:-1]
        ip.close()
        print len(ip_src)
        result=[]
        X = np.loadtxt("tmp.csv", delimiter=",", ndmin=0)
        y_pred =Birch(n_clusters=p1, threshold=p2).fit_predict(X)
        print 'birch--'
        print metrics.calinski_harabaz_score(X,y_pred)
        brich= [[] for c in range(p1)]
        for i in xrange(len(y_pred)):
                brich[y_pred[i]].append(ip_src[i])
        for i in range(p1):
                print len(brich[i]), brich[i]
                result.append((brich[i]))
        csvfile = file(os.getcwd() + "/result/tbrich/" + str(p1) + '--' + str(p2) + " clusters=" + str(p1) + '.csv',
                       'ab+')
        writer = csv.writer(csvfile)
        writer.writerows(result)
        csvfile.close()
