#Import python libraries
import numpy as np
import matplotlib.pyplot as plt
#Below line won't work since we don't hv the lab_utils_uni file, hence we won't get desired output
#from lab_utils_uni import plt_intution,plt_stationary,plt_update_onclick,soup_bowl

#Define the input,output variables
x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])
# Let 
w = 190
b = 100
#Define the function
def compute_cost(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w*x[i]+b
    return f_wb

tmp_cost = compute_cost(x_train,w,b)
plt.plot(x_train,tmp_cost,c='b',label='Our prediction')
plt.scatter(x_train,y_train,marker='x',c='r',label='Actual Value')
plt.title("Housing Prices")
plt.xlabel('Size')
plt.ylabel('Price')
plt.legend()
plt.show()

#For cost function(Not in this code)
# def calc_cost(x,y,w,b):
#     m = x.shape[0]
#     cost_sum = 0
#     for i in range(m):
#         f_wb = w*x[i]+b
#         cost_sum += (f_wb - y[i]) ** 2
#     total_cost = (1/(2*m)) * cost_sum
#     return total_cost