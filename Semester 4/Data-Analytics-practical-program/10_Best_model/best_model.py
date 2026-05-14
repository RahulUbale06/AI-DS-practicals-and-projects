# 10. Find the Best Model for Predicting Bike Rental
# Use Grid Search to find the best model (linear vs ridge) for bike demand prediction.
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

model = Ridge()

parameters = {
    'alpha': [0.1, 1, 10]
}

grid = GridSearchCV(model, parameters)

print("Grid Search Ready")