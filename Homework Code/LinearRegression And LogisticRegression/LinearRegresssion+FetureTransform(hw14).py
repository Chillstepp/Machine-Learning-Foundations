import numpy as np
import random


def generateData(rangex, rangey, amount, noiseRate):
    data_x1 = np.random.uniform(rangex, rangey, amount)
    data_x2 = np.random.uniform(rangex, rangey, amount)
    data_y = np.array([np.sign(data_x1[i]*data_x1[i] + data_x2[i]*data_x2[i] - 0.6) for i in range(amount)])
    data_y = data_y * np.where(np.random.random(amount) < noiseRate, -1, 1)
    data_x = []
    for i in range(amount):
        data_x.append([1, data_x1[i], data_x2[i]])
    return np.array(data_x), data_y.T

def linearRegression(data_x, data_y):
    return np.linalg.inv(np.dot(data_x.T, data_x)).dot(data_x.T).dot(data_y)

def featureTransform(oldData_x):
    data_x = []
    for i in range(oldData_x.shape[0]):
        x = oldData_x[i][1]
        y = oldData_x[i][2]
        data_x.append([1] + [x, y, x*y, x*x, y*y])
    return np.array(data_x)

def calSuccessRate(data_x, w):
    success = 0
    for x in data_x:
        if np.dot(x, w)*np.sign(x[1]*x[1] + x[2]*x[2] - 0.6) > 0:
            success += 1
    return success/data_x.shape[0]

if __name__ == '__main__':
    Eout_best = 1
    w_best = []
    for i in range(1000):
        data_x, data_y = generateData(-1, 1, 1000, 0.1)
        data_x = featureTransform(data_x)
        w = linearRegression(data_x, data_y)
        Eout = 1 - calSuccessRate(data_x, w)
        if Eout > Eout_best:
            Eout_best = Eout
            w_best = w
    print(w)
    print(Eout)

    '''
    [-0.98169133 -0.02749635 -0.01889739  0.02729206  1.52168933  1.51092938]
    error rate : 4%
    '''


    #error rate：about 51.6%
