# 1-D array
import numpy as np
n=np.array([1,2,3,4,5])
print(n)
print(n.ndim)

# 2-D array
import numpy as np
n1=np.array([[1,2,3,4],[1,2,3,4]])
print(n1)
print(n1.ndim)

# 3-D array
import numpy as np
n2=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(n2)
print(n2.ndim)

# n-D array
import numpy as np
n=np.array([1,2,3,4],ndmin=10)
print(n)
print(n.ndim)