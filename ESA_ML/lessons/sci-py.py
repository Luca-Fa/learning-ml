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

# As we know, Machine learning rarely works with 1D arrays, so let's create a 2D array
# To have a context, lets say our data represent the age and the weight of 5 people
dataset = np.array([[25,105],[30,68],[42,85],[3,17],[77,82]])

# Now that we know how to create and manipulate arrays it is time to apply this to Pandas

"""
2. Pandas Fundamentals
"""

# we will create a dataframe using the previous dataset context adding names to the five people
ages = dataset[:,0] # fetches all the rows and the first column (age)
weights = dataset[:,1] # fetches all the rows and the second column (weight)
names = ['John','Mary','Peter','Sally','Paul']

people = pd.DataFrame({'Name': names, 'Age': ages, 'Weight': weights})
# We have now created a proper dataframe using external arrays
# Now, lets put this data into a usable CSV file, without the idexes column to make it a real CSV file.
people.to_csv('ESA_ML\\datasets\\people.csv', index=False)

# Now let's read the CSV
people_from_file = pd.read_csv('ESA_ML\\datasets\\people.csv')
print(people_from_file)
# Result:
###     Name  Age  Weight
### 0   John   25     105
### 1   Mary   30      68
### 2  Peter   42      85
### 3  Sally    3      17
### 4   Paul   77      82
# The result is satisfying

# Now lets analyze our new dataFrame
print(people_from_file.info())
# What if we wanted to see its details
print(people_from_file.describe())

# Lets now begin the work of data scientist
# The objective is to load the dataset, calculate the mean, max and min of the ages and weights, and plot a graph of the data

ex_dataset = pd.read_csv('ESA_ML\\datasets\\people.csv')

age_mean = ex_dataset['Age'].mean()
age_min = ex_dataset['Age'].min()
age_max = ex_dataset['Age'].max()

weight_mean = ex_dataset['Weight'].mean()
weight_min = ex_dataset['Weight'].min()
weight_max = ex_dataset['Weight'].max()

plt.scatter(ex_dataset['Age'], ex_dataset['Weight'], color='blue', label='Data Points')

plt.xlabel('Age')
plt.ylabel('Weight')
plt.title('Weight evolution with age')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

"""
Now that we have reviewed the basics of our libraries, lets complete a mini project to put our knowledge into practice.
See you at ESA_ML\\projects\\spectral_analysis\\README.md for the next steps.
"""