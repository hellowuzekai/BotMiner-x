# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from __future__ import  division
import os

global TP
global FN
global FP
global TN
global ipCount
ipCount = 0
TP =0
TN = 0
FP = 0
FN = 0

def calAll(filePath):
    global TP
    global FN
    global FP
    global TN
    file = open(filePath, 'r')
    dataResult = file.read().split("\n")[:-1]
    file.close()
    for row in dataResult:
        calRight(row)
    print "******************* ip zong shu : "+str(ipCount)+" **************************"
    print "******************* TP: " + str(TP) + "***********************"
    print "******************* FN: " + str(FN) + "***********************"
    print "******************* FP: " + str(FP) + "***********************"
    print "******************* TN: " + str(TN) + "***********************"
    print "******************* TPR: " + str(TP/(TP+FN)) + "***********************" #分类其识别出的正实例占所有正实例的比率
    print "******************* FPR: " + str(FP/(FP+TN)) + "***********************" # 分类器错认为正类的负实例占所有负实例的比例 bot中的正常机占所有正常机 误报
    print "******************* ACC: " + str((TP+TN)/ipCount) + "***********************"    #正的预测正的 副的预测成副的
    print "******************* loubao: " + str(FN/(FN+TP)) + "***********************"
def calRight(row):
    global TP
    global FN
    global FP
    global TN
    tempRow = row.split(',')
    botCount = 0
    oneLength = len(tempRow)
    global ipCount
    ipCount += oneLength
    for tm in xrange(len(tempRow)):
        ipSub = tempRow[tm].split('.')[0]
        if ipSub.count('172') > 0:
            botCount += 1
    if float(botCount) / oneLength > 0.4:
        TP+=botCount
        FP += (oneLength - botCount)
    else:
        TN += (oneLength - botCount)
        FN += botCount


calAll(os.getcwd() + '/result.csv')