# 5.Summarize Mobile Usage Patterns
# Use descriptive statistics to summarize call durations and data usage per day from mobile
# logs.

import pandas as pd
data = {
    "call_duration" :[60,60,40,34,23,2,34],
    "data_usage" : [3,4,2,3,2,3,4]
}
df = pd.DataFrame(data)
print(df.describe())