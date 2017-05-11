# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from __future__ import division
import os

global TP
global FN
global FP
global TN
global ipCount
ipCount = 0
TP = 0
TN = 0
FP = 0
FN = 0


class Result:
    TP = 0
    FN = 0
    FP = 0
    TN = 0
    ipCount = 0

    def __init__(self, TP, FN, FP, TN, ipCount):
        Result.FP = FP
        Result.FN = FN
        Result.TN = TN
        Result.TP = TP
        Result.ipCount = ipCount


def calAll(filePath):
    result = Result(0, 0, 0, 0, 0)
    file = open(filePath, 'r')
    dataResult = file.read().split("\n")[:-1]
    file.close()
    for row in dataResult:
        calRight(row, result)
    return result


def calRight(row, result):
    tempRow = row.split(',')
    botCount = 0
    oneLength = len(tempRow)
    result.ipCount += oneLength
    for tm in xrange(len(tempRow)):
        ipSub = tempRow[tm].split('.')[0]
        if ipSub.count('172') > 0:
            botCount += 1
    if float(botCount) / oneLength > 0.5:
        result.TP += botCount
        result.FP += (oneLength - botCount)
    else:
        result.TN += (oneLength - botCount)
        result.FN += botCount
