import csv, os
import numpy as np
import random
from numpy import genfromtxt
from LinearRegression.linreg import LinearRegression
import math
import matplotlib.pyplot as plt

#NOTE: Closed fit works better, but gradient descent avoids inverting matricies

lr = LinearRegression()

# Example data from lecture slides
x_data = [.86, .09, -.85, .87, -.44, -.43, -1.1, .4, -.96, .17]
y_data = [2.49, .83, -.25, 3.1, .87, .02, -.12, 1.81, -.83, .43]
x0 = [1]*len(x_data)
X = np.transpose(np.array([x0, x_data]))
y = np.transpose(np.array([y_data]))
#lr.compare_error(X, y, .05, .0000001)

# Synthetic data from a linear function
y = lambda x: 10*x -10
x_data = [i for i in range(10)]
x0 = [1]*len(x_data)
X = np.transpose(np.array([x0, x_data]))
y = np.transpose(np.array([map(y, x_data)]))
#lr.compare_error(X, y, .0045, .0000000000000000001)


# Assignment data
data_dir = "data/OnlineNewsPopularity"
csv_path = os.path.join(data_dir, "OnlineNewsPopularity.csv")
csv = genfromtxt(csv_path, delimiter=', ', skip_header=1)
r, c = csv.shape

X_train = []
X_test = []
y_train = []
y_test = []
test_portion =0.30
for i in csv:
        rd = random.random()
        if rd < test_portion: 
            spl = np.array_split(i, [1, 60])
            X_test.append(spl[1])
            y_test.append(spl[2])
            
        else :
            spl = np.array_split(i, [1, 60])
            X_train.append(spl[1])
            y_train.append(spl[2])

X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)

error =[[],[]]
min_result = 2e+50

#h_split_1 = int(.33*r)
#csv = csv[:, [1,29,60]] # Only keeps some rows
#arrays = [np.array_split(csv, [1, 60], axis=1) for i in np.array_split(csv, [h_split_1,2*h_split_1], axis=0)] #TODO: Ask Pineau about removing the first column?
#urls = [i[0] for i in arrays]
#X_train = arrays[0][1]
#X_test = arrays[1][1]
#y_train = arrays[0][2]
#y_test = arrays[1][2]
#urls = [i[0] for i in arrays]
#for i in range(1,25) :
#   for j in range(1):
#        result = lr.compare_error(X_train, y_train, X_valid, y_valid, math.pow(10,-17), .01,math.pow(2,-i))[0][0]
#        error[0].append(result)
#        error[1].append(1/(math.pow(2,i)))
#        if result < min_result   :
#            min_i =i
#            min_result=result
#        print result
#print min_result, min_i
i=17
ret_closed, ret_grad= lr.compare_error(X_train, y_train, X_test, y_test, math.pow(10,-i), .000001,0)
print ret_closed,ret_grad
i=1
grad=[]
closed=[]
train=[]
min_size = min(len(ret_grad),len(ret_closed),len(y_train))
#Makes sure all arrays have the same length
while (i<min_size):
    if i%1==0:
        grad.append(ret_grad[i])
        closed.append(ret_closed[i])
        train.append(y_train[i])
    i=i+1
#plt.plot(range(len(ret_y)),ret_y,'ro', range(len(ret_y)),ret_x,'bs')
p1 = plt.plot(range(len(grad)),grad,'bs',markersize=5) # Plots the predictions for Gradient descent
#p2 = plt.plot(range(len(a)),b,'ro',markersize=3)
p3 = plt.plot(range(len(grad)),train,'yo',markersize=5) # Plots the real values of the training set
#plt.plot(range(len(ret_x)),ret_x,'bs',range(len(ret_y)),ret_y,'ro')

#plt.plot(error[1], error[0], 'ro')
#plt.xscale('log',basex=10)
#plt.axis([1,0,0,1.53170261e+8])
plt.title('Predicting the number of shares')
plt.ylabel('Number of shares')
plt.xlabel('Index (0 = most recent article)')
#plt.legend([p1, p2], ["Gradient descent prediction", "Actual number of shares"])
plt.show()
