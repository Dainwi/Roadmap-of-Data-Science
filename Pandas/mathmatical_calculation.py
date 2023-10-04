import pandas as pd

df = pd.read_csv('data.csv')

print(f'Sum of the column a is\n{df["a"].sum()}')