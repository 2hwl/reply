import numpy as np
import time
from scipy.optimize import linprog

start = time.time()

q = 332900
A = np.array([[2, 1], [-2, -1], [1, 1], [-1, -1], [0, 1], [0, -1], [-1, 1], [1, -1], [-2, 1], [2, -1]])

b = np.array([2.5, -1.5, 1.5, -0.5, 0.5, 0.5, -0.5, 1.5, -1.5, 2.5])

res = linprog(c=[0, 0], A_ub=A, b_ub=b)

print(res.x)
print(int(res.x[0]*q/2), int(res.x[1]*16))

end = time.time()
cost = end - start
print("average: {}".format(cost))
