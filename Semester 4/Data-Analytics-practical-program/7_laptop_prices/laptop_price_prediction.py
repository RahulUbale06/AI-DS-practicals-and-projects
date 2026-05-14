# 7. Predict Laptop Prices Based on Features
# Use multiple linear regression to predict laptop prices based on RAM, processor speed,
# and brand.
import warnings

warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'RAM': [4, 8, 16, 32],
    'Speed': [2.0, 2.5, 3.0, 3.5],
    'Price': [30000, 45000, 60000, 80000]
}

df = pd.DataFrame(data)

X = df[['RAM', 'Speed']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[16, 3.0]])

print(f"Predicted Price: {pred[0]:.2f}")