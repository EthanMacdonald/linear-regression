import csv, os
import numpy as np
from numpy import genfromtxt
from LinearRegression.linreg import LinearRegression

#NOTE: Closed fit works better, but gradient descent avoids inverting matricies

lr = LinearRegression()

# Example data from lecture slides
x_data = [.86, .09, -.85, .87, -.44, -.43, -1.1, .4, -.96, .17]
y_data = [2.49, .83, -.25, 3.1, .87, .02, -.12, 1.81, -.83, .43]
x0 = [1]*len(x_data)
X = np.transpose(np.array([x0, x_data]))
y = np.transpose(np.array([y_data]))
# lr.compare_error(X, y, .05, .0000001)

# Synthetic data from a linear function
y = lambda x: 10*x -10
x_data = [i for i in range(10)]
x0 = [1]*len(x_data)
X = np.transpose(np.array([x0, x_data]))
y = np.transpose(np.array([map(y, x_data)]))
# lr.compare_error(X, y, .0045, .0000000000000000001)

# Assignment data
data_dir = "data/OnlineNewsPopularity"
csv_path = os.path.join(data_dir, "OnlineNewsPopularity.csv")
csv = genfromtxt(csv_path, delimiter=', ', skip_header=1)
r, c = csv.shape
h_split_1 = int(.33*r)
h_split_2 = int(.66*r)
arrays = [np.array_split(csv, [1, 60], axis=1) for i in np.array_split(csv, [h_split_1, h_split_2], axis=0)] #TODO: Ask Pineau about removing the first column?
urls = [i[0] for i in arrays]
X_train = arrays[0][1]
X_valid = arrays[1][1]
X_test = arrays[2][1]
y_train = arrays[0][2]
y_valid = arrays[1][2]
y_test = arrays[2][2]
lr.compare_error(X_train, y_train, X_valid, y_valid, .00000000000000004, .01)