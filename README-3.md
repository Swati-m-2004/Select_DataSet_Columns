# Task 18 - Select Dataset Columns Using Pandas `loc` and `iloc`

## Overview
This project demonstrates how to select specific rows and columns from a Pandas DataFrame using `loc` and `iloc`.

**Internship:** AI & ML Track  
**Level:** 1  
**Day:** 18  
**Task:** Select Dataset Columns  
**Tools:** Python, Pandas, Jupyter Notebook

## Objective
The objective is to understand how to access specific parts of a DataFrame using:

- `loc` for label-based selection
- `iloc` for integer-position-based selection

## Dataset
The project uses the **Iris dataset** available through `scikit-learn`. It contains measurements of iris flowers and their species.

Columns used:
- `sepal_length`
- `sepal_width`
- `petal_length`
- `petal_width`
- `species`

## Requirements

Install the required libraries:

```bash
pip install pandas scikit-learn
```

Jupyter Notebook is recommended for an interactive demonstration:

```bash
pip install notebook
jupyter notebook
```

## How to Run

### Option 1: Python file

```bash
python task18_select_dataset_columns.py
```

### Option 2: Jupyter Notebook

1. Open Jupyter Notebook.
2. Create a new Python notebook.
3. Copy the code into cells.
4. Run the cells one by one.
5. Observe the selected rows and columns.

## Important Concepts

### 1. `loc`
`loc` selects data using row/column **labels**.

Example:

```python
df.loc[:, "sepal_length"]
```

This selects the column named `sepal_length`.

Multiple columns:

```python
df.loc[:, ["sepal_length", "petal_length", "species"]]
```

Rows and columns:

```python
df.loc[0:4, ["sepal_length", "sepal_width", "species"]]
```

### 2. `iloc`
`iloc` selects data using **integer positions**.

Example:

```python
df.iloc[:, 0]
```

This selects the first column.

Multiple columns:

```python
df.iloc[:, 0:3]
```

Rows and columns:

```python
df.iloc[0:5, 0:3]
```

## `loc` vs `iloc`

| Feature | `loc` | `iloc` |
|---|---|---|
| Selection method | Labels | Integer positions |
| Example | `df.loc[:, "species"]` | `df.iloc[:, 4]` |
| Column reference | Column name | Column number |
| Best used when | Names/labels are known | Positions are known |

## Project Structure

```text
task18_select_dataset_columns/
│
├── task18_select_dataset_columns.py
├── README.md
└── Task_18_Select_Dataset_Columns_Report.pdf
```

## Expected Output

The program displays:

- First few Iris records
- A single column selected with `loc`
- Multiple columns selected with `loc`
- Selected rows and columns with `loc`
- Conditional selection with `loc`
- A single column selected with `iloc`
- Multiple columns selected with `iloc`
- Selected rows and columns with `iloc`
- Final selected records

## Interview Questions

### 1. What is the difference between `loc` and `iloc`?
`loc` is mainly label-based, while `iloc` is integer-position-based.

### 2. How do you select a single column in Pandas?
```python
df["column_name"]
```
or:
```python
df.loc[:, "column_name"]
```

### 3. How do you select multiple columns?
```python
df[["column1", "column2"]]
```
or:
```python
df.loc[:, ["column1", "column2"]]
```

### 4. How do you select the first three columns using `iloc`?
```python
df.iloc[:, 0:3]
```

## Result
The task successfully demonstrates how Pandas can be used to access and extract specific rows and columns from a dataset using both `loc` and `iloc`.
