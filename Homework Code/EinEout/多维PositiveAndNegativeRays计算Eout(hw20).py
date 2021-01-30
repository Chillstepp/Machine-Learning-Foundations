#和19题差别只有测试数据集的更换
import numpy as np
import random

def generateData(path):
    data = open(path)
    num = 0
    for line in data:
        num = len(line.split()) - 1
        break
    data_x = [[] for i in range(num)]
    data_y = []
    for line in data:
        lineSplit = line.split()
        data_y.append(float(lineSplit[-1]))
        for _ in range(num):
            data_x[_].append(float(lineSplit[_]))
    dimension = num
    return data_x, data_y, dimension


def calEinThetaSign(data_x, data_y):
    thetaRange = [float('-inf')] + [(data_x[i]+data_x[i+1])/2 for i in range(data_x.shape[0]-1)] + [float('inf')]
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
    data_x, data_y, dimension = generateData("hw2_train.dat")
    thetas = []
    signs = []
    for i in range(dimension):
        _, theta, sign = calEinThetaSign(np.array(data_x[i]), np.array(data_y))
        thetas.append(theta)
        signs.append(sign)
    print(thetas)
    print(signs)
    data_test = open("hw2_test.dat")
    ans_true = 0
    ans_false = 0
    for line in data_test:
        true_times = 0
        false_times = 0
        for count in range(dimension):
            theta = thetas[count]
            sign = signs[count]
            linesplit = line.split()
            linesplit = [float(_) for _ in linesplit]
            if linesplit[count] < theta and sign == -1:
                false_times += 1
            elif linesplit[count] < theta and sign == 1:
                true_times += 1
            elif linesplit[count] > theta and sign == -1:
                true_times += 1
            elif linesplit[count] > theta and sign == 1:
                false_times += 1
            count += 1
        if true_times > false_times and linesplit[-1] == 1:
            ans_true += 1
        elif true_times > false_times and linesplit[-1] == -1:
            ans_false += 1
        elif true_times < false_times and linesplit[-1] == -1:
            ans_true += 1
        elif true_times < false_times and linesplit[-1] == 1:
            ans_false += 1
    print(ans_false/(ans_true+ans_false))
    #error rate：about 35%
