import numpy as np

# specify the input
np.random.seed(420)
n_obs = 1000
n_dim = 5
beta = np.array([1,0,1,0,1])

# make some random numbers
X = np.random.normal(size=(n_obs,n_dim))
y = X.dot(beta) + np.random.normal(size = n_obs) 

# the OLS estimator
def compute_ols(X, y, constant = True, resid = False) :

	if constant : X = np.hstack([np.ones((X.shape[0],1)), X])

	XX = X.T @ X
	Xy = X.T@y
	betahat = np.linalg.solve(XX, Xy)

	if resid : 
		return betahat
	else :
		resid = y - X@betahat
		return betahat, resid

# try it out
betahat, resid = compute_ols(X,y, resid = True)

print(
	'The beta hat is:\n', betahat, 
	'\n\nThe first ten residuals are:\n', resid[0:10]
	)