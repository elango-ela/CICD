import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

df = pd.read_csv("data/raw/breast_cancer_v1.csv")
df.to_csv("data/raw/data.csv", index=False)
