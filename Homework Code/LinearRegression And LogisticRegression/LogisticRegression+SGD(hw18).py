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

def calGradian_SGD(w, data_x, data_y):
    N = data_x.shape[0]
    i = random.randint(0, N-1)
    new_w = sigmoid(-data_y[i] * np.dot(w, data_x[i])) * (-data_y[i] * data_x[i])
    return new_w

def interation_w(w, eta, data_x, data_y, interation_amount):
    ww = w
    for i in range(interation_amount):
        ww = ww - eta*calGradian_SGD(ww, data_x, data_y)
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
    [[ 0.00228294]
     [ 0.04281966]
     [-0.02364879]
     [ 0.01486498]
     [-0.01436024]
     [ 0.03316679]
     [ 0.06201337]
     [-0.01865564]
     [ 0.02719088]
     [ 0.07015533]
     [ 0.01922508]
     [-0.01209169]
     [-0.00116996]
     [ 0.06421845]
     [ 0.06959673]
     [ 0.07491314]
     [-0.04332063]
     [ 0.07140024]
     [-0.01409018]
     [-0.01906695]]

    error rate: 0.477
    '''

