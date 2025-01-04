#Special numpy array functon..

# zeros function
import numpy as np
arr_zero=np.zeros(4)
arr_dim=np.zeros((4,4))
print(arr_zero)
print()
print(arr_dim)

# ones function
arr_zero=np.ones(4)
print(arr_zero)
arr_dim=np.ones((4,3))
print(arr_dim)

# Create Empty function 
arr_emp=np.empty(3)
print(arr_emp)

# Range function
arr_range=np.arange(4)
print(arr_range)

# Diagonal function
arr_diag=np.eye(4)
print(arr_diag)

# Linspace function
arr_ls=np.linspace(0,20,num=5)
print(arr_ls)
