import numpy as np
var=np.array([1,2,3,4],dtype=np.int64)
print(var.dtype)

var1=np.array([1.3,11.2,23.3,5.4])
print(var1.dtype)

var2=np.array(["H","E","L","L","O"])
print(var2.dtype)

var3=np.array([2,3,4,5],dtype="f")
print(var3.dtype)

var4=np.array([4,5,6,7])
new=np.float32(var4)
print(var4.dtype)
print(new.dtype)
print(var4)
print(new)

var5=np.array([3,4,5,6])
new1=var5.astype(float)
print(var5)
print(new1)