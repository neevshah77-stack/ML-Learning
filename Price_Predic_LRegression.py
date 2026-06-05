import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])
w = 200
b = 100
def compute_model_output(x,w,b):
  m = x.shape[0]
  f_wb = np.zeros(m)
  for i in range(m):
    f_wb[i] = w * x[i] + b

  return f_wb

tmp_f_wb = compute_model_output(x_train,w,b,)

plt.plot(x_train,tmp_f_wb,c='b',label='Our prediction')
plt.scatter(x_train,y_train,marker='o',c='r',label='Acutal Values')
plt.title("Housing Prices")
plt.ylabel('Price')
plt.xlabel('Size')
plt.legend()
plt.show()

#For x = 1.2
x_i = 1.2
cost = w*x_i + b
print(f"${cost:.0f} thousand dollars")