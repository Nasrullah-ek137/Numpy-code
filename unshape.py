import numpy as np
var=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a=var.reshape(2,3,2)
print(a)
b=var.reshape(-1)
print(b)