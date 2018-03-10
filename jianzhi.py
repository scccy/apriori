import pandas as pd
import numpy as np

df = pd.read_excel("地震.xls")
df["location"] = df["参考地名"].str.slice(start=0, stop=2)
df["time"] = df["日期"].str.slice(start=0, stop=7)
df = df.drop(["日期", "参考地名"], axis=1)
train_data = np.array(df)
train_x_list = train_data.tolist()#分割每条数据

def createC2(dataSet):
    C1 = []
    for transaction in dataSet:
        for n in range(len(transaction)):
            item = transaction[n]
            if not [item] in C1:
                C1.append([item]) #store all the item unrepeatly

    #return map(frozenset, C1)#frozen set, user can't change it.
    return list(map(frozenset, C1))


def scand(D,Ck):#计算support总量
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                # if not ssCnt.has_key(can):
                if not can in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(D))
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems  # compute support
        supportData[key] = support
    return supportData


def scanD(D,Ck,minSupport):
    ssCnt={}
    for tid in D:
        if can.issubset(tid):
            #if not ssCnt.has_key(can):
            if not can in ssCnt:
                ssCnt[can]=1
            else: ssCnt[can]+=1
    numItems=float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems #compute support
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData


def rb(dataSet, minSupport=0.6):
    C1 = createC2(dataSet)
    D = list(map(set, dataSet))
    supportData_value_list = []
    supportData = scanD(D, C1，minSupport)
    for n in supportData:
        values = supportData[n]
        supportData_value_list.append(values)
    r = min(supportData_value_list)/max(supportData_value_list)
    return r


def suppor_all(dataSet):
    pass

# def all_confidence(l, supportData, minsuppot = 0.3):
#     C1 = createC2(dataSet)
#     D = list(map(set, dataSet))
#     supportData_value_list = []
#     supportData =

def life():
    pass

df = [["2","3","4"], ["2","4","5"], ["4","6"]]

print(rb(df))