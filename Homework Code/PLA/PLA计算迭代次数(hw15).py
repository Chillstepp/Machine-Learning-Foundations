import numpy as np


class PLA(object):
    def __init__(self, dimension, count):
        self.__dimension = dimension
        self.__count = count

    def trainSetSplit(self, path):
        training_set = open(path)
        x_train = np.zeros((self.__count, self.__dimension))
        y_train = np.zeros((self.__count, 1))
        x = []
        x_count = 0
        for num, line in enumerate(training_set):
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
                    w += y_train[i, :] * x_train[i, :].reshape(self.__dimension, 1)
                    ans += 1
                    flag = False
            if flag:
                break
        return ans

if __name__ == '__main__':
    perceptron = PLA(5, 400)
    print(perceptron.interation_num("hw1_15_train.dat"))
    #ans = 45
