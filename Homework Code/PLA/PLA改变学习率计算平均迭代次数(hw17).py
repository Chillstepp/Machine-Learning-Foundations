import numpy as np
import random

class PLA(object):
    def __init__(self, dimension, count):
        self.__dimension = dimension
        self.__count = count

    def trainSetSplit(self, path):
        training_set = open(path)
        training_set_list = []
        for num, line in enumerate(training_set):
            training_set_list.append(line)
        random.shuffle(training_set_list)
        x_train = np.zeros((self.__count, self.__dimension))
        y_train = np.zeros((self.__count, 1))
        x = []
        x_count = 0
        for num, line in enumerate(training_set_list):
            x.append(1)
            for i in range(0, len(line.split())):
                if i < len(line.split())-1:
                    x.append(line.split()[i])
                else:
                    y_train[num, 0] = line.split()[i]
            x_train[num, :] = x
            x = []
        return x_train, y_train


    def interation_num(self, path):
        ans = 0
        x_train, y_train = self.trainSetSplit(path)
        w = np.zeros((self.__dimension, 1))
        while True:
            flag = True
            for i in range(self.__count):
                if np.dot(x_train[i, :], w) * y_train[i, 0] <= 0:
                    w += 0.5*y_train[i, :] * x_train[i, :].reshape(self.__dimension, 1)#多了一个learning rate=0.5
                    ans += 1
                    flag = False
            if flag:
                break
        return ans

if __name__ == '__main__':
    perceptron = PLA(5, 400)
    sum = 0
    for i in range(2000):
        sum += perceptron.interation_num("hw1_15_train.dat")
    print(sum/2000)
    #about 40.125 times interation
