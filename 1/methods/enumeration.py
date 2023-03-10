import numpy as np
from utils import count_data


def enumeration(interval_x1, interval_x2, f, accuracy):
    n = count_data(accuracy)
    X1 = np.linspace(interval_x1[0], interval_x1[1], n)
    X2 = np.linspace(interval_x2[0], interval_x2[1], n)

    min_x1_x2 = (X1[0], X2[0])
    for i in range(n):
        if f(X1[i], X2[i]) < f(min_x1_x2[0], min_x1_x2[1]):
            min_x1_x2 = (X1[i], X2[i])

    return min_x1_x2
