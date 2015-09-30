import numpy as np

#REF: Numpy library
#REF: COMP 598 Lecture slides
#REF: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html to make sure I didn't miss any important methods - I didn't look at any code!

class LinearRegression(object):

	def __init__(self, copy=True):
		self.copy = copy

	def closed_fit(self, X, y, reg_factor):
		# Closed form fit using matrix inversion
		if self.copy:
			X = np.copy(X)
			y = np.copy(y)
		r, c = X.shape
		self.w = np.linalg.inv(np.transpose(X).dot(X)+reg_factor*np.identity(c)).dot(np.transpose(X)).dot(y)
		return np.copy(self.w)

	def gradient_fit(self, X, y, alpha, err, reg_factor):
		# Gradient descent fit
		if self.copy:
			X = X.copy()
			y = y.copy()
		r, c = X.shape
		w0 = np.transpose(np.array([[1]*c]))    
		self.w = self._next_weight(w0, X, y, alpha,reg_factor)
		flag=0
		while np.sum(abs(w0 - self.w))/len(w0) > err:
			w0 = self.w
			#for i in w0:
                         #       if np.isinf(i):
                          #              flag=1
                        #if flag==1:
                         #       break
			self.w = self._next_weight(w0, X, y, alpha,reg_factor)
		return self.w

	def _next_weight(self, w, X, y, alpha,reg_factor):
		# Helper function for gradient_fit method
		#print w
		return w - alpha*(np.transpose(X).dot(X).dot(w)-np.transpose(X).dot(y)) - (alpha*reg_factor*w)

	def predict(self, X):
		# Predicts an output for a given X
		if not self.w.any():
			raise Exception("Please train LinearRegression object before making predictions")
		elif self.copy:
			X = np.copy(X)
                prediction = X.dot(self.w)
		for row in prediction: # We cannot have a negative number of shares!
                        for element in xrange(len(row)):
                                if row[element] <0:
                                        row[element]=0
		return prediction

	def test(self, X, Y):
		# Reports the Mean Squared Error on a test set
		if self.copy:
			X = X.copy()
			Y = Y.copy()
		inner = Y - self.predict(X)
		r, c = inner.shape
		err = np.transpose(inner).dot(inner)/r
		return err

	def compare_error(self, X_train, y_train, X_test, y_test, alpha, err,reg_factor):
		# Compares gradient descent error and closed form error
		self.gradient_fit(X_train, y_train, alpha, err,reg_factor)
		gradient_test = self.test(X_train, y_train)
		gradient_test2 = self.test(X_test,y_test)
		grad_predict = self.predict(X_test)
		print "Gradnt Err: " + str(self.test(X_train,y_train))
		print self.w
		self.closed_fit(X_train, y_train,reg_factor)
		closed_test = self.test(X_test, y_test)
		print "Closed Err: " + str(self.test(X_train,y_train))
		print self.w
		closed_predict = self.predict(X_test)
		#return closed_predict, grad_predict # Returns closed prediction and grad prediction
                return grad_predict, closed_predict
