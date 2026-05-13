# 2. Import and Summarize COVID-19 Cases Data
# Import a CSV file of district-wise COVID-19 cases and print basic summaries like total
# cases, deaths, and recovery rates.

import pandas as pd

data = {
    "district":['A','B','C'],
    "Cases":[1000,1500,1200],
    "Deaths":[50,70,30],
    "recovered":[10,10,10]
}

df = pd.DataFrame(data)
total_cases  = df['Cases'].sum()
total_deaths = df['Deaths'].sum()
total_recovered = df['recovered'].sum()

recovered_percent = (total_recovered / total_cases)* 100
print("TOTAL CASES : ",total_cases)
print("TOTAL DEATHS : ",total_deaths)
print("RECOVERY RATE : ",total_recovered)
