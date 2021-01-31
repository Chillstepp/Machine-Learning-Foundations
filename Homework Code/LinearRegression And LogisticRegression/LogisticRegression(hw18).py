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
    w = interation_w(w, 0.001, data_x, data_y, 2000)
    amount = 0
    print(w)
    error_times = 0
    data_x_test, data_y_test, amount_test = splitData("hw3_test.dat")
    for i in range(amount_test):
        if np.dot(data_x_test[i], w) * data_y_test[i] < 0:
            error_times += 1
    print(error_times / amount_test)

    '''
    [[-0.01106136  0.04234835 -0.03109114  0.0165552  -0.03514716  0.01407574
   0.049675   -0.02056954  0.02630158  0.07051782  0.02089157 -0.01836243
  -0.00716701  0.04758432  0.05944894  0.06276506 -0.04569257  0.06224517
  -0.01461797 -0.03329689]]
    
    error rate: 0.4716666666666667
    '''

