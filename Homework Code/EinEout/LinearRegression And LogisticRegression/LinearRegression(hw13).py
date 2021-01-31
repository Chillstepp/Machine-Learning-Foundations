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

def calSuccessRate(data_x, w):
    success = 0
    for x in data_x:
        if np.dot(x, w)*np.sign(x[1]*x[1] + x[2]*x[2] - 0.6) > 0:
            success += 1
    return success/data_x.shape[0]

if __name__ == '__main__':
    Eout = 0
    for i in range(1000):
        data_x, data_y = generateData(-1, 1, 1000, 0.1)
        w = linearRegression(data_x, data_y)
        Eout += 1 - calSuccessRate(data_x, w)
    print(Eout/1000)

    #error rate：about 51.6%
