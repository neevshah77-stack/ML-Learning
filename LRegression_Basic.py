#Import python libraries
import numpy as np
import matplotlib.pyplot as plt

#Define input,output variables
x_train = np.array([1.0,2.0])
print(f"x_train = {x_train}")
y_train = np.array([300.0,500.0])
print(f"y_train = {y_train}")

#Shows size of input
print(f"x_train.shape = {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training elements: {m}")
#Prints x,y at i=1
i=1
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}),y^({i})) = ({x_i},{y_i})")

plt.scatter(x_train,y_train,marker='o',c='g')#.scatter plots datapoints
#Sets title and all
plt.title("Housing Prices")
plt.ylabel('Price')
plt.xlabel('Size')
plt.show()