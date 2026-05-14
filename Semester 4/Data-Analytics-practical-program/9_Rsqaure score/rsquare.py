# 9. Evaluate a Model Using R-Squared
# Calculate R-squared and MSE to evaluate how well your model predicts house prices.
from sklearn.metrics import r2_score, mean_squared_error

y_true = [10,20,30,40,50]
y_pred = [11,24,31,43,52]

r2  = r2_score(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)

print(f"R2_score : {r2}")
print(f"MSE : {mse}")