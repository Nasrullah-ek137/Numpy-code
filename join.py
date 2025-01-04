# 1-D array..
import numpy as np
var=np.array([1,2,3,4,5])
var1=np.array([9,8,7,6,5])
c=np.concatenate((var,var1))
print(c)

print()

# 2-D array..
a=np.array([[1,2,3,4,5],[2,4,6,8,10]])
b=np.array([[0,1,3,5,7],[5,10,15,20,25]])
co=np.concatenate((a,b),axis=1)
print(co)
print()


# 3-D array..
ax=np.array([[[7,14,21],[2,4,6],[10,20,30]]])
con=np.concatenate((ax),axis=1)
print(con)