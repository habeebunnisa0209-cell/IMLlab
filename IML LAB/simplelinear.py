
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv("hours_marks_data.csv")
# Independent and Dependent variables
X = data['Hours'].values
Y = data['Marks'].values
n = len(X)
# Mean of X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)
# Calculate Slope (b1)
numerator = np.sum((X - mean_x) * (Y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
b1 = numerator / denominator
# Calculate Intercept (b0)
b0 = mean_y - b1 * mean_x
# Print results
print("Slope (b1):", b1)
print("Intercept (b0):", b0)
# Predict Y values
Y_pred = b0 + b1 * X
# Calculate Mean Squared Error
mse = np.mean((Y - Y_pred) ** 2)
print("Mean Squared Error (MSE):", mse)
# Ask user input
x_new = float(input("Enter value of X to predict Y: "))
y_new = b0 + b1 * x_new
print("Predicted Y value:", y_new)
# Plot graph
plt.scatter(X, Y)            # Actual data points
plt.plot(X, Y_pred)          # Regression line
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Simple Linear Regression Graph")
plt.show()
