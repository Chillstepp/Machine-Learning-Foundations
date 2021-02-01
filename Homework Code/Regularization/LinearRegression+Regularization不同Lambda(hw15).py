import numpy as np
import random
import math

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
    Ein_min = 1
    Eout_min = 1
    Ein_lambda = 0
    Eout_lambda = 0
    for lamda in [pow(10, mi) for mi in range(-10, 3)]:
        w = cal_w_Regulaizaion(data_x, data_y, lamda)
        Ein = calErrorRate(w, "hw4_train.dat")
        Eout = calErrorRate(w, "hw4_test.dat")
        if Eout <= Eout_min:
            Eout_min = Eout
            Eout_lambda = lamda
            Ein_min = Ein
    print(math.log10(Eout_lambda), Ein_min, Eout_min)

    #print(Eout_lambda, Eout_min)
    '''
    lambda = -7
    Ein = 0.03
    Eout = 0.015
    '''

