from pathlib import Path
import pandas as pd

# Find CSV path
csv_path = Path("data/adsb.csv")

# Load the CSV into memory as a table
df = pd.read_csv(csv_path)

# Inspect dataset 
print("\nShape (rows, cols):", df.shape)
print("\nColumns:")
print(list(df.columns))
print("\nFirst 5 rows:")
print(df.head())
