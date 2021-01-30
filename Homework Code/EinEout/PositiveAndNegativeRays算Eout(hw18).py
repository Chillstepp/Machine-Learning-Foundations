import numpy as np
import random

def generateData(rangex, rangey, amount, noiseRate):
    data_x = np.sort(np.random.uniform(rangex, rangey, amount))
    #noise
    data_y = np.sign(data_x)*np.where(np.random.random(data_x.shape[0]) < noiseRate, -1, 1)
    return data_x, data_y


def calEinThetaSign(data_x, data_y):
    thetaRange = [-1] + [(data_x[i]+data_x[i+1])/2 for i in range(data_x.shape[0]-1)] + [-1]
    thetaRange = np.array(thetaRange)
    sign_ans = 0
    Ein_ans = 0
    theta_ans = 0
    for theta in thetaRange:
        true_count = 0
        sign_left = -1
        for i in range(data_x.shape[0]):
            if data_x[i] < theta and data_y[i] == -1:
                true_count += 1
            elif data_x[i] > theta and data_y[i] == 1:
                true_count += 1
            Ein = true_count/data_x.shape[0]
        if Ein < 0.5:
            Ein = 1 - Ein
            sign_left = 1
        if Ein > Ein_ans:
            Ein_ans = Ein
            sign_ans = sign_left
            theta_ans = theta
    return 1 - Ein_ans, theta_ans, sign_ans

    

if __name__ == '__main__':
    Eout = 0
    for i in range(5000):
        data_x, data_y = generateData(-1, 1, 20, 0.2)
        x, theta, sign = calEinThetaSign(data_x, data_y)
        Eout = Eout + 0.5 + 0.3 * sign * (abs(theta) - 1)
    print(1 - Eout/5000)
    #error rate：about 26%
