import pandas as pd
import numpy as np

# Ensure reproducible dataset generation
np.random.seed(42)

rows = []

# Reference spectral signatures for each mineral
minerals = {
    "Olivine":     [0.72, 0.65, 0.34, 0.82, 0.91],
    "Pyroxene":    [0.32, 0.45, 0.86, 0.54, 0.42],
    "Basalt":      [0.55, 0.58, 0.60, 0.57, 0.54],
    "Anorthosite": [0.82, 0.79, 0.40, 0.30, 0.25]
}

# Create a balanced mineral distribution
mineral_pool = []

for mineral in minerals.keys():
    mineral_pool.extend([mineral] * 200)

# Randomize mineral assignment
np.random.shuffle(mineral_pool)

# Generate spectral samples
for sample_id in range(1, 801):

    mineral = mineral_pool[sample_id - 1]

    base_signature = minerals[mineral]

    # Simulate measurement noise
    spectrum = np.array(base_signature) + np.random.normal(
        loc=0,
        scale=0.03,
        size=5
    )

    # Keep values within a realistic range
    spectrum = np.clip(spectrum, 0, 1)

    rows.append([
        f"R{sample_id:04d}",
        mineral,
        *spectrum
    ])

# Build dataframe
df = pd.DataFrame(
    rows,
    columns=[
        "sample_id",
        "mineral",
        "w450",
        "w550",
        "w650",
        "w750",
        "w850"
    ]
)

# Define spectral measurement columns
spectral_columns = [
    "w450",
    "w550",
    "w650",
    "w750",
    "w850"
]

# Inject missing values to simulate sensor failures
for _ in range(30):

    random_row = np.random.randint(0, len(df))
    random_column = np.random.choice(spectral_columns)

    df.loc[random_row, random_column] = np.nan

# Inject outliers to simulate corrupted measurements
for _ in range(10):

    random_row = np.random.randint(0, len(df))
    random_column = np.random.choice(spectral_columns)

    df.loc[random_row, random_column] = np.random.choice([
        -2.0,
        3.5,
        5.0,
        7.0
    ])

# Export dataset
df.to_csv(
    "ESA_ML\\datasets\\projects\\spectral-analysis\\spectral_samples.csv",
    index=False
)

# Display generation summary
print("Dataset successfully created.")
