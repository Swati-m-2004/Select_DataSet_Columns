# Task 18 - Select Dataset Columns using Pandas loc and iloc
# AI & ML Internship - Level 1, Day 18
#
# Requirements:
#   pip install pandas scikit-learn
#
# Run in Jupyter Notebook or as a Python script.

import pandas as pd
from sklearn.datasets import load_iris

# ---------------------------------------------------------
# 1. Load the Iris dataset
# ---------------------------------------------------------
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
    ],
)

# Add the target/species column
df["species"] = [iris.target_names[i] for i in iris.target]

print("=" * 60)
print("IRIS DATASET")
print("=" * 60)
print(df.head())


# ---------------------------------------------------------
# 2. Examples using loc
# loc = label-based selection
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("LOC EXAMPLES")
print("=" * 60)

# Example 1: Select one column by its label
print("\n1. Select one column using loc:")
print(df.loc[:, "sepal_length"])

# Example 2: Select multiple columns by their labels
print("\n2. Select multiple columns using loc:")
print(df.loc[:, ["sepal_length", "petal_length", "species"]])

# Example 3: Select rows by label/index and columns by label
print("\n3. Select first five rows and selected columns using loc:")
print(df.loc[0:4, ["sepal_length", "sepal_width", "species"]])

# Example 4: Select rows where petal length is greater than 5
print("\n4. Conditional selection using loc:")
print(df.loc[df["petal_length"] > 5, ["petal_length", "petal_width", "species"]].head(10))


# ---------------------------------------------------------
# 3. Examples using iloc
# iloc = integer-position-based selection
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("ILOC EXAMPLES")
print("=" * 60)

# Example 1: Select first column
print("\n1. Select first column using iloc:")
print(df.iloc[:, 0])

# Example 2: Select first three columns
print("\n2. Select first three columns using iloc:")
print(df.iloc[:, 0:3])

# Example 3: Select first five rows and first three columns
print("\n3. Select first five rows and first three columns using iloc:")
print(df.iloc[0:5, 0:3])

# Example 4: Select specific rows and columns by integer positions
print("\n4. Select specific rows and columns using iloc:")
print(df.iloc[[0, 2, 4], [0, 2, 4]])


# ---------------------------------------------------------
# 4. Direct column selection
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("DIRECT COLUMN SELECTION")
print("=" * 60)

print("\nSingle column:")
print(df["species"].head())

print("\nMultiple columns:")
print(df[["sepal_length", "sepal_width", "species"]].head())


# ---------------------------------------------------------
# 5. Final selected records
# ---------------------------------------------------------
selected_records = df.loc[10:14, ["sepal_length", "petal_length", "species"]]

print("\n" + "=" * 60)
print("FINAL SELECTED RECORDS")
print("=" * 60)
print(selected_records)

print("\nTask completed successfully!")
