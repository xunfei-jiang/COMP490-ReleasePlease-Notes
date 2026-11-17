import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise multiplication: [4, 10, 18]
element_wise = a * b

# Dot product / matrix multiplication: 32
matrix_mult = a @ b
