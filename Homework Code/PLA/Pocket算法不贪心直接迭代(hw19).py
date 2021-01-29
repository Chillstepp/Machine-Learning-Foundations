import numpy as np
import random

class Pocket(object):
    def __init__(self, dimension, count_train, count_test):
        self.__dimension = dimension
        self.__count_train = count_train
        self.__count_test = count_test

    def trainSetSplit(self, path):
        training_set = open(path)
        training_set_list = []
        for num, line in enumerate(training_set):
            training_set_list.append(line)
        random.shuffle(training_set_list)
        x_train = np.zeros((self.__count_train, self.__dimension))
        y_train = np.zeros((self.__count_train, 1))
        x = []
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


    def interation_w(self,interation_times, path):
        x_train, y_train = self.trainSetSplit(path)
        w = np.zeros((self.__dimension, 1))
        maxx = 0
        cnt = 0
        update_time = 0
        while True:
            if np.dot(x_train[cnt, :], w) * y_train[cnt, 0] <= 0:
                w += y_train[cnt, :] * x_train[cnt, :].reshape(self.__dimension, 1)
                update_time += 1
                cnt += 1
                if(update_time == interation_times or cnt == self.__count_train):
                    break
            else:
                cnt += 1
                if (update_time == interation_times or cnt == self.__count_train):
                    break
        return w

    def test(self, w_test, path, count):
        x_test, y_test = self.trainSetSplit(path)
        true_times = 0
        for i in range(count):
            if np.dot(x_test[i, :], w_test) * y_test[i, 0] > 0:
                true_times += 1
        return true_times/count


if __name__ == '__main__':
    perceptron = Pocket(5, 500, 500)
    sum = 0
    for i in range(2000):
        w = perceptron.interation_w(50, "hw1_18_train.dat")
        t = perceptron.test(w, "hw1_18_test.dat", 500) #正确率
        #print(t)
        sum += (1-t) #错误率累加
        print(i, 1-t)
    print(sum/2000)
    #error rate：about 35%
