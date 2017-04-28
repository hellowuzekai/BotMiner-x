# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import Birch


def get_cflow_data(group_id):
    """
    Fetch all cflow data from database
    """

    import MySQLdb
    db = MySQLdb.connect('localhost', 'root', '5610346', 'BOTNET')
    cursor = db.cursor()
    sql = "select * from Cflow where GROUP_ID={} order by id".format(group_id)
    cflows = cursor.fetchmany(cursor.execute(sql))
    print "[database] cflows: {}".format(len(cflows))

    return cflows


# test
if __name__ == '__main__':
    cflows = get_cflow_data(group_id=1)
    cflows += get_cflow_data(group_id=2)
    ip_src = []
    f = open("tmp.csv" ,"w+")
    ip = open("ip.csv","w+")
    for i in xrange(len(cflows)):
        # f.write(cflows[i][7]+','+cflows[i][8]+','+cflows[i][9]+','+cflows[i][10]+"\n")
        f.write(cflows[i][8] + ',' + cflows[i][9] + ',' + cflows[i][10] + "\n")
        ip.write(cflows[i][2]+"\n")
    f.close()
    ip.close()
    ip = open("ip.csv" ,"r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    print len(ip_src)
    print ip_src
    X = np.loadtxt("tmp.csv", delimiter=",", skiprows=0, ndmin=2)
    # plt.scatter(X[:, 0], X[:, 1], marker='*', c='r',s = 1)
    # plt.show()

    # y_pred = Birch().fit_predict(X)
    # plt.scatter(X[:, 0], X[:, 1], marker='*', c=y_pred,s = 10)
    # plt.show()
    # print "Calinski-Harabasz Score", metrics.calinski_harabaz_score(X, y_pred)

    # print "3："
    # y_pred = Birch(n_clusters=4, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(3):
    #     print len(brich[i]), brich[i]
    # print "4："
    # y_pred = Birch(n_clusters=4, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(4):
    #     print len(brich[i]), brich[i]
    # print "5："
    # y_pred = Birch(n_clusters=5, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(5):
    #     print len(brich[i]), brich[i]
    # print "6："
    # y_pred = Birch(n_clusters=6, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(6):
    #     print len(brich[i]), brich[i]
    # print "7："
    # y_pred = Birch(n_clusters=7, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(7):
    #     print len(brich[i]), brich[i]
    # print "8："
    # y_pred = Birch(n_clusters=8, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [], [], []]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(8):
    #     print len(brich[i]), brich[i]

    # print "9："
    # y_pred = Birch(n_clusters=36, threshold=0.1).fit_predict(X)
    # brich = [[], [], [], [], [], [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # for i in xrange(len(y_pred)):
    #     brich[y_pred[i]].append(ip_src[i])
    # for i in range(36):
    #     print len(brich[i]), brich[i]
    # print y_pred
    # plt.scatter(X[:, 0], X[:, 1], marker='*', c=['b','r','g'])
    # for i in xrange(len(ip_src)):
    #     plt.annotate(ip_src[i], xy=(y_pred[i], 0), xytext=(-20, 20),
    #                 textcoords='offset points', ha='center', va='bottom',
    #                 bbox=dict(boxstyle='round,pad=0.2', fc='red', alpha=0.1))
    #                 # arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',
    #                 #                 color='red'))
    # plt.show()
    # print 'Calinski-Harabasz Score', metrics.calinski_harabaz_score(X, y_pred)
    #
    # y_pred = Birch(n_clusters=6, threshold=0.1).fit_predict(X)
    # type1 = plt.scatter(X[:, 0], X[:, 1], marker='*', c=y_pred)
    # plt.show()
    # print 'Calinski-Harabasz Score', metrics.calinski_harabaz_score(X, y_pred)
    #
    # y_pred = Birch(n_clusters=6, threshold=0.1, branching_factor=30).fit_predict(X)
    # plt.scatter(X[:, 0], X[:, 1], marker='*', c=y_pred)
    # plt.show()
    # print 'Calinski-Harabasz Score', metrics.calinski_harabaz_score(X, y_pred)
    #
    #
