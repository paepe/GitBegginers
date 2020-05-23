import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
y = np.array([1, 2, 1, 3, 2.5, 2, 5])

# Create linear regression object
regr = LinearRegression()
regr.fit(x, y)  # Dont wrap it in []

# And then again at prediction time:
y_result = regr.predict([[2000]])
y_result_mtx = regr.predict(np.array([125, 2000, 313]).reshape(-1, 1))

print(y_result, y_result_mtx)
