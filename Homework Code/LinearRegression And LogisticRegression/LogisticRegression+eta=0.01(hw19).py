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
        for i in range(len(linesplit)-1):
            data_x[_].append(float(linesplit[i]))
        data_y.append(float(linesplit[-1]))
    return np.array(data_x),np.array(data_y),amount

def sigmoid(s):
    return 1/(1+np.exp(-s))

def calGradian(w, data_x, data_y):
    N = data_x.shape[0]
    sum = 0
    for i in range(N):
        sum += sigmoid(-data_y[i]*np.dot(w, data_x[i]))*(-data_y[i]*data_x[i])
    return 1/N*sum

def interation_w(w, eta, data_x, data_y, interation_amount):
    ww = w
    for i in range(interation_amount):
        ww = ww - eta*calGradian(ww, data_x, data_y)
    return ww.T


if __name__ == '__main__':
    data_x, data_y, amount_train = splitData("hw3_train.dat")
    w = np.zeros((1, data_x[0].shape[0]))
    w = interation_w(w, 0.01, data_x, data_y, 2000)
    amount = 0
    print(w)
    error_times = 0
    data_x_test, data_y_test, amount_test = splitData("hw3_test.dat")
    for i in range(amount_test):
        if np.dot(data_x_test[i], w) * data_y_test[i] < 0:
            error_times += 1
    print(error_times / amount_test)

    '''
    [[-0.18939478]
     [ 0.26593156]
     [-0.35382514]
     [ 0.04066458]
     [-0.37976253]
     [ 0.01954328]
     [ 0.33365205]
     [-0.26415962]
     [ 0.13465748]
     [ 0.49115247]
     [ 0.0870017 ]
     [-0.25574013]
     [-0.16317915]
     [ 0.30043823]
     [ 0.39986173]
     [ 0.43193814]
     [-0.46251163]
     [ 0.43202779]
     [-0.20813247]
     [-0.3696613 ]]
    
    error rate: 0.22066666666666668
    '''

