import numpy as np
import pandas as pd
n = 200
data = {
    "Student_ID": np.arange(1, n+1),
    "Daily_Screen_Time": np.random.randint(60, 600, n),  # minutes
    "Academic_Usage": np.random.randint(10, 70, n),      # percentage
    "Social_Media_Usage": np.random.randint(10, 60, n),  # percentage
    "Gaming_Usage": np.random.randint(5, 40, n),         # percentage
    "Device_Type": np.random.choice(["Android", "iOS"], n),
    "Internet_Access_Type": np.random.choice(["Wi-Fi", "Mobile Data"], n),
    "Peak_Usage_Hours": np.random.randint(1, 24, n)      # hours in 24h format
}

df = pd.DataFrame(data)
df.to_csv("STUDENT_DATA.csv", index=False)

print(df.head())
device_ratio = df["Device_Type"].value_counts(normalize=True) * 100
print("Device Preference Ratio (%):\n", device_ratio)
internet_ratio = df["Internet_Access_Type"].value_counts(normalize=True) * 100
print("Internet Access Type (%):\n", internet_ratio)
peak_hours = df["Peak_Usage_Hours"].value_counts().sort_index()
print("Peak Usage Hours Distribution:\n", peak_hours)
df["Non_Academic_Usage"] = df["Social_Media_Usage"] + df["Gaming_Usage"]

academic_trend = df["Academic_Usage"].mean()
non_academic_trend = df["Non_Academic_Usage"].mean()

print("Average Academic Usage (%):", academic_trend)
print("Average Non-Academic Usage (%):", non_academic_trend)