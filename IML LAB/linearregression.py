import csv
import math
import matplotlib.pyplot as plt

x = []
y = []

# Read data from CSV file
with open("Temperature_vs_IceCream_Sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

n = len(x)

# Calculate sums
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i] * y[i] for i in range(n))
sum_x2 = sum(xi**2 for xi in x)

# Calculate slope (b) and intercept (a)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

# ✅ Display slope and intercept clearly
print("\nSlope (b):", round(b, 3))
print("Intercept (a):", round(a, 3))
print("Regression Equation: Y = {:.3f} + {:.3f}X".format(a, b))

# User input for prediction
x_new = float(input("\nEnter X value to predict Y: "))
y_pred = a + b * x_new
print("Predicted Y value:", round(y_pred, 3))

# Error calculation (RMSE)
mse = sum((y[i] - (a + b * x[i]))**2 for i in range(n)) / n
rmse = math.sqrt(mse)
print("Error Rate (RMSE):", round(rmse, 4))

# Graph plotting
y_line = [a + b * xi for xi in x]

plt.scatter(x, y)
plt.plot(x, y_line)
plt.xlabel("Temperature")
plt.ylabel("Ice Cream Sales")
plt.title("Simple Linear Regression")
plt.show()

