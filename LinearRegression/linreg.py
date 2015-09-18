import numpy as np

#REF: Numpy library
#REF: COMP 598 Lecture slides
#REF: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html to make sure I didn't miss any important methods - I didn't look at any code!

#TODO: Regularization (optional)
#TODO: Extra features (optional)
#TODO: Optimize matrix operations (optional)

class LinearRegression(object):

	def __init__(self, copy=True):
		self.copy = copy

	def closed_fit(self, X, y, regularize=False):
		# Closed form fit using matrix inversion
		if self.copy:
			X = np.copy(X)
			y = np.copy(y)
		self.w = np.linalg.inv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(y)
		return np.copy(self.w)

	def gradient_fit(self, X, y, alpha, err, regularize=False):
		# Gradient descent fit
		if self.copy:
			X = X.copy()
			y = y.copy()
		r, c = X.shape
		w0 = np.transpose(np.array([[1]*c]))
		self.w = self._next_weight(w0, X, y, alpha)
		while np.sum(abs(w0 - self.w))/len(w0) > err:
			w0 = self.w
			self.w = self._next_weight(w0, X, y, alpha)
		return self.w

	def _next_weight(self, w, X, y, alpha):
		# Helper function for gradient_fit method
		return w - alpha*(np.transpose(X).dot(X).dot(w)-np.transpose(X).dot(y))

	def predict(self, X):
		# Predicts an output for a given X
		if not self.w.any():
			raise Exception("Please train LinearRegression object before making predictions")
		elif self.copy:
			X = np.copy(X)
		return X.dot(self.w)

	def test(self, X, Y):
		# Reports the Mean Squared Error on a test set
		if self.copy:
			X = X.copy()
			Y = Y.copy()
		inner = Y - self.predict(X)
		r, c = inner.shape
		err = np.transpose(inner).dot(inner)/r
		return err

	def compare_error(self, X_train, y_train, X_test, y_test, alpha, err):
		# Compares gradient descent error and closed form error
		self.gradient_fit(X_train, y_train, alpha, err)
		gradient_test = self.test(X_test, y_test)
		self.closed_fit(X_train, y_train)
		closed_test = self.test(X_test, y_test)
		# Print results of comparison
		print "Gradnt Err: " + str(gradient_test)
		print "Closed Err: " + str(closed_test)