# Spectral Analysis Project

*Educational project inspired by planetary spectroscopy and scientific data analysis.*

## Overview

This project is an introduction to scientific data analysis through a simulated multispectral dataset.

The objective is to explore, visualize and understand spectral measurements collected from different rock samples. While no machine learning model is used yet, this project reproduces the data exploration phase commonly performed before developing classification algorithms.

The workflow follows a typical scientific process:

1. Load the dataset
2. Inspect and validate the data
3. Compute descriptive statistics
4. Visualize spectral signatures
5. Compare samples
6. Detect anomalies
7. Explore correlations between spectral bands

---

## Project Structure

```text
ESA_ML/projects/spectral-analysis/
├── spectral_analysis.py
├── spectral_dataset_generator.py
└── README.md

ESA_ML/datasets/projects/spectral-analysis/
└── spectral_samples.csv
```

---

## Dataset Description

The dataset contains several simulated rock samples.

Each sample is described by its mineral class and spectral response at different wavelengths.

| Column | Description |
|----------|----------|
| sample_id | Sample identifier |
| mineral | Mineral class |
| w450 | Intensity measured at 450 nm |
| w550 | Intensity measured at 550 nm |
| w650 | Intensity measured at 650 nm |
| w750 | Intensity measured at 750 nm |
| w850 | Intensity measured at 850 nm |

Example:

```text
sample_id,mineral,w450,w550,w650,w750,w850
R0001,Olivine,0.72,0.65,0.34,0.82,0.91
```

---

## Learning Objectives

By completing this project, the following skills are developed:

- Loading datasets with Pandas
- Data inspection and validation
- Descriptive statistics
- Missing value detection
- Scientific data visualization
- Spectral signature comparison
- Correlation analysis
- Basic anomaly detection

---

## Spectral Signatures

A spectral signature represents the response of a material measured at different wavelengths.

For example:

```text
450 nm → 0.72
550 nm → 0.65
650 nm → 0.34
750 nm → 0.82
850 nm → 0.91
```

The shape of the resulting curve can help distinguish different materials.

---

## Dataset Characteristics

The generated dataset contains approximately 800 spectral samples belonging to four simulated mineral classes:

- Olivine
- Pyroxene
- Basalt
- Anorthosite

To reproduce realistic scientific datasets, the data intentionally includes:

- Missing spectral measurements
- Outlier values
- Measurement noise

These imperfections allow the implementation of data cleaning and validation procedures before further analysis.

---

## Objectives

The purpose of this analysis is to answer the following questions:

- Are there missing values in the dataset?
- Are there abnormal measurements?
- Do some spectral bands exhibit strong correlations?
- Can different minerals be distinguished through their spectral signatures?

---

## Why This Project?

The project is inspired by scientific workflows used in planetary exploration and remote sensing.

Understanding spectral data is an important step before building machine learning models capable of identifying minerals, rocks or other geological materials.

This project serves as preparation for future machine learning exercises involving:

- Spectral classification
- Mineral recognition
- Data fusion
- Scientific machine learning

---

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Expected Outputs

The analysis should produce:

- Summary statistics
- Missing value reports
- Correlation matrices
- Spectral signature plots
- Outlier detection visualizations

The generated outputs help understand the structure and quality of the dataset before applying machine learning techniques.

---

## Next Step

After this exploratory analysis, the next stage consists of training a machine learning model capable of automatically classifying spectral samples based on their measurements.

Future projects will introduce:

- Data preprocessing
- Feature engineering
- Classification algorithms
- Model evaluation
- Deep learning techniques
- Planetary mineral recognition