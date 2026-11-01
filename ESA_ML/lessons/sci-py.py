"""
==================================================
SCIENTIFIC PYTHON
Preparation for Machine Learning
==================================================

Contents

1. Introduction
2. NumPy Fundamentals
3. Pandas Fundamentals
4. Data Exploration
5. Visualization with Matplotlib
6. Mini Project
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
1. NumPy Fundamentals
"""

# The usual array
numbers = np.array([1,5,6,7,8,9,777])
#                   0-1-2-3-4-5--6
print(numbers)

# Accessing elements
print(numbers[0])
#             ^ This number is the key in the array

# Statistics
print("Mean:", numbers.mean())
print("Max:", numbers.max())
print("Min:", numbers.min())

# Excercice 1: with the list of temperatures below, calculate and print the mean, max and min temperatures only
# temperatures: 21,23,51,28,41,32,26,16,17,16,16,8,-6
temperatures = np.array([21,23,51,28,41,32,26,16,17,16,16,8,-6])

print("Mean:", temperatures.mean(),"Min:",temperatures.min(),"max:",temperatures.max())
