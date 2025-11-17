import numpy as np
import matplotlib.pyplot as plt 
# sample dataset 
X = np.array([1,2,3,4,5])
y = np.array([2.2,4.8,9.1,16.3,25.5])
# normalize X for stability 
X_norm = X/max(X)
# intialize parameters 
a = 0.0
b = 0.0
c = 0.0
lr = 0.1
epochs = 1000
n = len(X_norm)
# gradient descent 
for i in range(epochs):
    y_pred = a * X_norm**2+b * X_norm +c
    error = y_pred-y
# gradients 
da = (2/n) * np.sum(error * X_norm**2)
db = (2/n) * np.sum(error * X_norm)
dc = (2/n) * np.sum(error)
# updated parameters 
a -= lr * da
b -= lr * db
c -= lr * dc
# plot result 
plt.scatter(X, y, label="Data Points")
plt.plot(X, a*X_norm**2 + b*X_norm + c, color='red', label="Fitted Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Polynomial Regression using Gradient Descent")
plt.legend()
plt.show()

print(f"Learned parameters: a={a:.3f}, b={b:.3f}, c={c:.3f}")



