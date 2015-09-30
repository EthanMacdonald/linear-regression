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
data_dir = "data/reddit_dataset"
csv_path = os.path.join(data_dir, "full_data_final.csv")
csv = genfromtxt(csv_path, delimiter=',', skip_header=1)
r, c = csv.shape

X_train = []
X_test = []
y_train = []
y_test = []
test_portion =0.30
stop=0
for i in csv:
        stop = stop +1
        if  stop<92000:
                continue
        rd = random.random()
        if rd < test_portion: 
            spl = np.array_split(i, [1, 10])
            X_test.append(spl[1])
            y_test.append(spl[2])
            
        else :
            spl = np.array_split(i, [1, 10])
            X_train.append(spl[1])
            y_train.append(spl[2])


print "Extraction done"
X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)

error =[[],[]]
min_result = 2e+50
min_i=0
#h_split_1 = int(.33*r)
#csv = csv[:, [1,29,60]] # Only keeps some rows
#arrays = [np.array_split(csv, [1, 60], axis=1) for i in np.array_split(csv, [h_split_1,2*h_split_1], axis=0)] #TODO: Ask Pineau about removing the first column?
#urls = [i[0] for i in arrays]
#X_train = arrays[0][1]
#X_test = arrays[1][1]
#y_train = arrays[0][2]
#y_test = arrays[1][2]
#urls = [i[0] for i in arrays
"""error_test=[[],[]]
for i in range(1,25) :
#   for j in range(1):
        result,result_test = lr.compare_error(X_train, y_train, X_test, y_test, math.pow(10,-i),0.000001,0)
        result = result[0][0]
        result_test=result_test[0][0]
        error[0].append(result)
        error[1].append(1/(math.pow(10,i)))
        error_test[0].append(result_test)
        error_test[1].append(1/(math.pow(10,i)))
        if result < min_result   :
            min_i =i
            min_result=result
        print result
print min_result, min_i
"""
i=14
ret_grad, ret_closed= lr.compare_error(X_train, y_train, X_test, y_test, math.pow(10,-i), .000001,0)
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
print len(grad)
#plt.plot(range(len(ret_y)),ret_y,'ro', range(len(ret_y)),ret_x,'bs')
p1 = plt.plot(range(len(grad)),grad,'bs',markersize=3, label='Gradient descent prediction') # Plots the predictions for Gradient descent
p2 = plt.plot(range(len(grad)),closed,'ro',markersize=3, label='Closed form prediction') # Plots the predictions for Closed Form
p3 = plt.plot(range(len(grad)),train,'yo',markersize=3, label='Actual score') # Plots the real values of the training set
#plt.plot(range(len(ret_x)),ret_x,'bs',range(len(ret_y)),ret_y,'ro')

#plt.plot(error[1], error[0], 'ro',markersize=3)
#plt.plot(error_test[1], error_test[0], 'bo',markersize=3)
#plt.xscale('log',basex=10)
#plt.yscale('log',basex=10)
#plt.axis([1,0,1e+3,5.53170261e+9])
plt.title('Score prediction of closed-form and gradient descent')
plt.ylabel('Score')
plt.xlabel('Index')
plt.legend(loc='upper left')
#plt.legend([p1, p2], ["Gradient descent prediction", "Actual number of shares"])
plt.show()
