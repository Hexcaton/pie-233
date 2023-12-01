import numpy as np

Z = np.ones((10,10))
print('Исходный вектор Z: \n', Z)
Z[1:-1,1:-1] = 0
print('Вектор Z с нулями внутри: \n', Z)