import numpy as np
import random


def splitData(path):
    txt = open(path)
    data_x = []
    data_y = []
    amount = 0
    for _, line in enumerate(txt):
        amount += 1
        linesplit = line.split()
        data_x.append([])
        data_x[_].append(float(1))
        for i in range(len(linesplit)-1):
            data_x[_].append(float(linesplit[i]))
        data_y.append(float(linesplit[-1]))
    return np.array(data_x),np.array(data_y),amount

def cal_w_Regulaizaion(Z, y, lamda):
    return np.linalg.inv(np.dot(Z.T, Z) + lamda*np.eye(3)).dot(Z.T).dot(y.T)

def calErrorRate(w, path):
    data_x, data_y, amount = splitData(path)
    false = 0
    for i, x in enumerate(data_x):
        if np.dot(x, w) * data_y[i] < 0:
            false += 1
    return false / amount

if __name__ == '__main__':
    data_x, data_y, amount_train = splitData("hw4_train.dat")
    w = cal_w_Regulaizaion(data_x, data_y, 10)
    Ein = calErrorRate(w, "hw4_train.dat")
    Eout = calErrorRate(w, "hw4_test.dat")
    print(Ein, Eout)
    '''
    Ein = 0.05
    Eout = 0.045
    '''

