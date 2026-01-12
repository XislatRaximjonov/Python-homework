import numpy as np

# Original list
my_list = [12.23, 13.32, 100, 36.32]

# Convert to 1D NumPy array
arr = np.array(my_list)

print("Original List:", my_list)
print("One-dimensional NumPy array:", arr)

import numpy as np

arr = np.arange(2, 11).reshape(3, 3)
print(arr)

import numpy as np

arr = np.zeros(10)
print(arr)

arr[6] = 11
print(arr)


import numpy as np

arr = np.arange(12, 38)
print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array as float:", float_arr)

import numpy as np

celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 1.8 + 32

print("Values in Celsius:", celsius)
print("Values in Fahrenheit:", fahrenheit)

import numpy as np

arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("Original array:", arr)
print("After append:", new_arr)

import numpy as np

arr = np.random.rand(10)

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

import numpy as np

arr = np.random.rand(10, 10)

print("Min:", arr.min())
print("Max:", arr.max())

import numpy as np

arr = np.random.rand(3, 3, 3)
print(arr)
