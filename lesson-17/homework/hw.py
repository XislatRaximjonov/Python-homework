import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1. Rename columns
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print first 3 rows
print(df.head(3))

# 3. Mean age
print("\nMean age:", df['age'].mean())

# 4. Select and print only name + city
print(df[['first_name', 'City']])

# 5. Add salary column with random values
df['Salary'] = np.random.randint(40000, 100000, size=len(df))
print("\nDataFrame with Salary:")
print(df)

# 6. Summary statistics
print("\nSummary statistics:")
print(df.describe())


import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print("Maximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

print("Minimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())


import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# Set Category as index
expenses = expenses.set_index('Category')

# Maximum expense for each category
print("Max expense by category:\n", expenses.max(axis=1))

# Minimum expense
print("\nMin expense by category:\n", expenses.min(axis=1))

# Average expense
print("\nAverage expense by category:\n", expenses.mean(axis=1))

