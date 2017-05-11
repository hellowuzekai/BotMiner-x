import os

import shutil
import CalC
from tbrich import tbrich
from tdbscan import tdbScan
from AffinityPropagation import AffinityPropagation, affinityPropagation
global kind
kind =""
DIR = os.getcwd() + "/result"


class Result:
    TP = 0
    FN = 0
    FP = 0
    TN = 0

    def __init__(self, TP, FN, FP, TN):
        Result.FP = FP
        Result.FN = FN
        Result.TN = TN
        Result.TP = TP


def sumResult(kind):
    fileList = os.listdir(os.getcwd() + "/result/" + kind + "/")
    fileList.sort(compare)
    for file in fileList:
        result = CalC.calAll(os.getcwd()+"/result/" +kind+"/"+ str(file))
        writResultFile(kind + 'sumResult.txt', str(file), result)
        print "is analysising " + str(file)


def compare(x, y):
    stat_x = os.stat(DIR+ "/" +kind+ "/" + x)
    stat_y = os.stat(DIR+ "/" +kind+ "/" + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0


def writResultFile(fileName, name, Result):
    file = open(os.getcwd() + '/' + fileName, 'ab+')
    j1 = "*******************" + name + "*******************"
    j1 += "\n ip zong shu : " + str(Result.ipCount)
    j1 += "\n TP: " + str(Result.TP)
    j1 += "\n FN: " + str(Result.FN)
    j1 += "\n FP: " + str(Result.FP)
    j1 += "\n TN: " + str(Result.TN)
    j1 += "\n TPR: " + str(float(Result.TP) / (Result.TP + Result.FN))
    j1 += "\n FPR: " + str(
        float(Result.FP) / (Result.FP + Result.TN))
    j1 += "\n ACC: " + str(float((Result.TP + Result.TN)) / Result.ipCount)
    j1 += "\n loubao: " + str(float(Result.FN) / (Result.FN + Result.TP))
    j1 += "\n\n"
    file.write(j1)
    file.close()


def affinitymain():
    para1 = -60
    para2 = 1.0
    i = -40
    global kind
    kind = 'affinity'
    while  i-para1 > 0:
        j = 0.5
        while j <= para2:
            affinityPropagation(i, j)
            j += 0.1
        i -= 1
    print "start analysis Data.........."
    sumResult("affinity")
    print "Done"



def tbrichmain():
    global kind
    kind = 'tbrich'
    para1 = 150
    para2 = 0.5
    i = 100
    while para1 - i > 0:
        j = 0.1
        while j <= para2:
            tbrich(i, j)
            j += 0.1
        i += 1
    print "start analysis Data.........."
    sumResult("tbrich")
    print "Done"


def tbscanmain():
    global kind
    kind = 'tbscan'
    para1 = 0.5
    para2 = 20
    i = 0.1
    while para1 - i > 0:
        j = 5
        while j <= para2:
            tdbScan(i, j)
            j += 1
        i += 0.1
    print "start analysis Data.........."
    sumResult("tbscan")
    print "Done"

def init():
    fileList =  os.listdir(os.getcwd()+"/result/")
    for j in fileList:
        if os.path.isdir(os.getcwd()+"/result/"+j):
            shutil.rmtree(os.getcwd()+"/result/"+j)
            os.mkdir(os.getcwd()+"/result/"+j)
    fList = os.listdir(os.getcwd())
    for f in fList:
        if str(f).count("sumResult")>0:
            os.remove(os.getcwd() + "/" + f)

init()
#affinitymain()
tbrichmain()
tbscanmain()