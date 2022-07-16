import numpy as np
import matplotlib.pyplot as plt

def est_coef(x,y):
	n=np.size(x)
	x_mean=np.mean(x)
	y_mean=np.mean(y)
	SS_xy=np.sum(y*x)-n*x_mean*y_mean
	SS_xx=np.sum(x*x)-n*x_mean*x_mean
	b_1=SS_xy/SS_xx
	b_0=y_mean-b_1*x_mean
	return (b_1,b_0)


def plot_linearRegression(x,y,b):
	plt.scatter(x,y,marker="o")
	y_pred=b[0]+b[1]*x
	plt.plot(x,y_pred)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()

if __name__ == "__main__":
	x=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	y=np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
	#coefficients finding
	b=est_coef(x,y)
	plot_linearRegression(x,y,b)