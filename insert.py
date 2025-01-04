# insert function..
import numpy as np
var=np.array([10,20,30,40])
v=np.insert(var,(1,4),(15,50))
print(v)

var1=np.array([[1,2,3],[1,2,3]])
i=np.insert(var1,3,[4,4],axis=1)
print(i)
print()

# delete function.
import numpy as np
var2=np.array([[1,2,3],[1,2,3]])
d=np.delete(var2,[0,0],axis=1)
print(d)