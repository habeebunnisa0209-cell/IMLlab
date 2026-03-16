import pandas as pd, numpy as np, matplotlib.pyplot as plt

data=pd.read_csv("hours_marks_data.csv")
X,Y=data['Hours'].values,data['Marks'].values
mx,my=np.mean(X),np.mean(Y)

b1=np.sum((X-mx)*(Y-my))/np.sum((X-mx)**2)
b0=my-b1*mx

print("Slope (b1):",b1)
print("Intercept (b0):",b0)

Yp=b0+b1*X
mse=np.mean((Y-Yp)**2)
print("Mean Squared Error (MSE):",mse)

x=float(input("Enter value of X to predict Y: "))
print("Predicted Y value:",b0+b1*x)

plt.scatter(X,Y); plt.plot(X,Yp)
plt.xlabel("Hours Studied"); plt.ylabel("Marks Scored")
plt.title("Simple Linear Regression Graph")
plt.show()
