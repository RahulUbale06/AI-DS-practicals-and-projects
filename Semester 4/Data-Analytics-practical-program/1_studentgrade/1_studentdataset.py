# Explore Student Grades Dataset
# Use Python to calculate average marks, highest and lowest scores from a CSV file of
# student grades.

import pandas as pd
data = {
    'Name' : ["Rahul","Somshekhar","Sumit","Prasad"],
    'Marks' : [78,85,67,92]
}
df = pd.DataFrame(data)
print(df)
print("Average marks: ", df['Marks'].mean())
print("Highest Marks: ",df['Marks'].max())
print("Lowest Marks: ",df['Marks'].min())
