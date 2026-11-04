"""
In this first project, we will simply analyse the generated data in:
     '\\ESA_ML\\datasets\\projects\\spectral-analysis\\spectral_samples.csv'
Try to find patterns in the data. 
The dataset contains 800 samples of spectral measurements for different minerals, 
with some missing values and outliers injected to simulate real-world scenarios.

For more details on the project, please refer to the README.md file in the project directory.

"""


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The first step would be: loading the dataset
# We will use pandas to read the CSV file

dataframe = pd.read_csv("ESA_ML\\datasets\\projects\\spectral-analysis\\spectral_samples.csv")
# Does it work ?
if dataframe is not None: 
    print("Data loaded successfully!")
    print(dataframe.head(), "...")

    # Now that we know the data is loaded, we can start exploring it.
    # First step: outliers detection and handling missing values.
    #   The objective is to exhibit all ouliers
    #   and missing values with their indexes

    # So, lets define what we consider an outlier in this context.
    # For this project, we will consider any value that is more than 3 standard deviations
    # away from the mean as an outlier. This is a common statistical rule of thumb

    # We will also calculate the average noise level in the dataset, which will help us to identify the outliers more accurately.

    # 1: Enumerate the number of missing values in the dataset
    #       Showing a table with the dataframe rows with missing values
    #       id | mineral | w450 | w550 | w650 | w750 | w850 | w950

    missing_values_ids = dataframe[dataframe.isnull().any(axis=1)].index.tolist()
    rows_with_missing_values = dataframe.loc[missing_values_ids]
    print("Here are the missing values\n", rows_with_missing_values)

    # By knowing the detected mineral, 
    # we can replace the missing values by the expected value 
    # which represent the typical spectral signature of that mineral.

    # In this way, we need to calculate the average intensity mesured for each mineral 
    # at each wavelength, and then use these averages to fill in the missing values.

    # Firstly, we have to know the unique menerals in the dataset
    unique_menierals = dataframe["mineral"].unique()
    print("Unique minerals in the dataset:\n", unique_menierals)

    # to calculate the avg intensity we also need to exclude the missing values from the calculation,
    # so we will use the dropna() function to remove any rows with missing values before calculating the averages.
    list_of_wavelenghts = ["w450", "w550", "w650", "w750", "w850"]

    avg_intensity_map = {} # {mineral: {wavelength: avg_intensity}}

    for mineral in unique_menierals:
        # Filter the dataframe to only include rows for the current mineral
        mineral_data = dataframe[dataframe["mineral"] == mineral].dropna()
        avg_intensity_map[mineral] = {}
        
        # Calculate the average intensity for each wavelength
        for wavelength in list_of_wavelenghts:
            avg_intensity = mineral_data[wavelength].mean()
            # Now we map the avg for further use
            avg_intensity_map[mineral][wavelength] = avg_intensity

    # Now the avg map is ready we can use it to fill the missing values
    for idx in missing_values_ids:
        mineral = dataframe.loc[idx, "mineral"]
        for wavelength in list_of_wavelenghts:
            if pd.isnull(dataframe.loc[idx, wavelength]):
                dataframe.loc[idx, wavelength] = avg_intensity_map[mineral][wavelength]

    # We can now check if there are still any missing values in the dataset
    if dataframe.isnull().sum().sum() == 0:
        print("All missing values have been filled successfully!")
        # Lets now define what is mathematically an outlier in this context.
        #     For this project, we will consider any value that is more than 3 standard deviations from the mean.
        #     Here is the expression:
        #       |value - mean| > 3 * std, std = sqrt(variance) and variance = sum((value - mean)^2) / n, where n is the number of values in the dataset.
        #     where 'mean' is the average value of the dataset and 'std' is the standard deviation of the dataset.

        # If we really have outliers, this means that minerals might have been misclassified
        # For the exercise, we have replaced missing values too early, and the calculation of the mean might be biased by the outliers, so we will have to recalculate the mean and std after removing the outliers.

        for row in dataframe.itertuples():
            for wavelength in list_of_wavelenghts:
                value = getattr(row, wavelength)
                mean = dataframe[wavelength].mean()
                std = dataframe[wavelength].std()
                if abs(value - mean) > 3 * std:
                    print(f"Outlier detected at index {row.Index} for wavelength {wavelength}: {value}")
                    # Remove the outlier from the dataset
                    dataframe = dataframe[dataframe[wavelength] != value]
                    # Lets expose the value vs the mean and std
                    print(f"-> Mean: {mean}, Std: {std}, Value: {value}")
                

    else:
        print("There are still some missing values in the dataset.")




