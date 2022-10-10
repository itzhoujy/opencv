import numpy as np
x1 = [[1,2,3],[4,5,6],[7,8,9]]
y1 = x1[2::]
print(y1)

x2 = np.array([[1,4,8,10],[2,6,9,10]])
y2 = x2[0:,2:]
print(y2)