# Search array function...
import numpy as np
var=np.array([1,2,3,4,5,6,7,8,9,0,0,8,7,6,2,2,2,3,4,5,4,3,4,6])
search=np.where((var)==2)
print(search)

# search sorted array
var1=np.array([1,2,3,4,6,7,8,9])
se=np.searchsorted(var1,5)
print(se)

# Shuffle function.
import numpy as np
var2=np.array([1,2,3,4,5])
np.random.shuffle(var2)
print(var2)

# Unique function..
import numpy as np
var3=np.array([1,2,3,4,5,2,3,4,2,2,1,3,4,6])
u=np.unique(var3,return_counts=True)
print(u)


# Resize function..
import numpy as np
var4=np.array([1,2,3,4,5,6])
r=np.resize(var4,(2,3))
print(r)

# Flatten function..
import numpy as np
var5=np.array([[1,2,3,4],[2,4,6,8]])
print(var5)
print(var5.ravel())  # [12342468]
print(var5.ravel(order="A")) # [12342468]
print(var5.ravel(order="F")) #  [1 2 2 4 3 6 4 8]
print(var5.ravel(order="K"))  # [1 2 3 4 2 4 6 8]
print(var5.ravel(order="C"))  # [1 2 3 4 2 4 6 8]
