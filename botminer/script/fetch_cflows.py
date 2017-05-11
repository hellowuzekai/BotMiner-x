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
    cflows += get_cflow_data(group_id=3)
    ip_src = []
    f = open("clusteringFinal/tmp.csv" ,"w+")
    ip = open("clusteringFinal/ip.csv","w+")
    for i in xrange(len(cflows)):
        # f.write(cflows[i][7]+','+cflows[i][8]+','+cflows[i][9]+','+cflows[i][10]+"\n")
        f.write(cflows[i][8] + ',' + cflows[i][9] + ',' + cflows[i][10] + "\n")
        ip.write(cflows[i][2]+"\n")
    f.close()
    ip.close()
    ip = open("clusteringFinal/ip.csv" ,"r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    print len(ip_src)