import numpy as np


def multiplication_matrix(n):
    numbers = np.arange(1, n + 1)
    return np.outer(numbers, numbers)

print(multiplication_matrix(3))
