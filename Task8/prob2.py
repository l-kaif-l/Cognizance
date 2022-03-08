# Problem 2

import numpy as np

a = []
b = []

L = int(input("Enter the length of the arrays"))

print("Enter first array elements")
for i in range(0, L):
    value = int(input())
    a.append(value)

print("Enter second array elements")
for i in range(0, L):
    value = int(input())
    b.append(value)

A = np.array(a)
B = np.array(b)

print("Array A ==", A, "\nArray B ==", B)
# Returns True if arrays are equal, False if arrays are not equal
print(np.array_equal(A, B))