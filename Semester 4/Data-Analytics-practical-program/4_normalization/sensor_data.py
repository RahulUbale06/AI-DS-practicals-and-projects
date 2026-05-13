# 4. Normalize Sensor Data from an IoT Device
# Normalize temperature and humidity readings collected from a sensor to a range between
# 0 and 1.

import pandas as pd

data = {
    "Temperature" : [34,35,36,37,38,39,40,41,42,43,44]
}
df = pd.DataFrame(data)

df['Normalize'] = (
    (df['Temperature'] - df['Temperature'].min()) /
    (df['Temperature'].max() - df['Temperature'].min())
)
print(df)