import numpy as np
import pandas as pd
df=pd.read_csv(r"E:\2ND-SEMESTER\DATA SCIENCE\ASSIGNMENT5\fraud_transactions_200.csv")
print(df.head())
def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# Apply normalization to "Amount" column
df["Amount_Normalized"] = min_max_normalize(df["Amount ($)"])
print(df.head())

Q1 = df["Amount ($)"].quantile(0.25)
Q3 = df["Amount ($)"].quantile(0.75)
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["Amount ($)"] < lower_bound) | (df["Amount ($)"] > upper_bound)]
print("Outliers:\n", outliers)


mean_value = df["Amount ($)"].mean()
df.loc[(df["Amount ($)"] < lower_bound) | (df["Amount ($)"] > upper_bound), "Amount ($)"] = mean_value
print(df.head())