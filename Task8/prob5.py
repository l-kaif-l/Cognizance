# Problem 5

import numpy as np

# Addition of arrays
A = np.array([9, 2, 7])
B = np.array([2, 5, 4])

print("1st array : ", A)
print("2nd array : ", B)

result = np.add(A, B)
print("Sum of the above arrays is : ", result)

# Multiplication of Matrices
# 2D arrays
m1 = np.array([[1, 4, 7], [2, 5, 8]])
m2 = np.array([[1, 4], [2, 5], [3, 6]])
print("\nm1:", m1, "\n\nm2:", m2)
m3 = np.dot(m1, m2)
print("\nm1*m2 =", m3)

# 3D arrays
m1 = ([1, 6, 5], [3, 4, 8], [2, 12, 3])
m2 = ([3, 4, 6], [5, 6, 7], [6, 56, 7])
print("\nm1:", m1, "\n\nm2:", m2)
m3 = np.dot(m1, m2)
print("\nm1*m2 =", m3)