import numpy as np
import matplotlib.pyplot as plt
from sklearn. linear_model import LinearRegression
np.random. seed(0)
x=2*np.random.rand(100,1)
y=4+3*x+np.random.randn(100,1)
model=LinearRegression()
model.fit(x,y)
x_new=np.array([[0], [2]])
y_pred=model.predict(x_new)
plt.scatter(x,y,color="blue", label="data points")
plt.plot( x_new, y_pred,color="red", label="Regression line")
plt.xlabel('x')
plt.ylabel('y')
plt.title("linear Regression")
plt.legend()
plt.show()