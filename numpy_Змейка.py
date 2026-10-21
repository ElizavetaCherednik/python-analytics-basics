import numpy as np


def snake(m, n, direction='H'):
    if direction == 'H':
        matrix = np.arange(1, m * n + 1, dtype=np.int16).reshape(n, m)
        matrix[1::2, :] = matrix[1::2, ::-1]
        return matrix
    else:
        matrix = np.arange(1, m * n + 1, dtype=np.int16).reshape(m, n).T
        matrix[:, 1::2] = matrix[::-1, 1::2]
        return matrix
print(snake(5, 3))
