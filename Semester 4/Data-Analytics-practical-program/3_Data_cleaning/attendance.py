# 3. Clean Attendance Records
# Fix missing values and incorrect entries (e.g., “AB” instead of 0) in a student attendance
# dataset.

import pandas as pd
import numpy as np
data = {
    "Name" :["Rahul","Sumit","Prasad"],
    "Attendance" :[99,0,np.nan]
}

df = pd.DataFrame(data)
df["Attendance"] = df['Attendance'].replace(0,'AB')
df["Attendance"] = df['Attendance'].fillna(0)

print(df)