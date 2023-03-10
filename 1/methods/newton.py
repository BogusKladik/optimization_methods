import numpy as np


def newton(x0, gradient, hessian, accuracy):
    min_x1_x2, x1_x2 = x0 - \
        np.dot(gradient(x0[0], x0[1]), np.linalg.inv(hessian())), x0

    while abs(min_x1_x2 - x1_x2).sum() >= len(min_x1_x2) * accuracy:
        x1_x2, min_x1_x2 = min_x1_x2, x1_x2 - \
            np.dot(gradient(x1_x2[0], x1_x2[1]), np.linalg.inv(hessian()))

    return min_x1_x2
