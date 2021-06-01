import numpy as np
arr = [0,0,3,0,0 ,0,0,1,0,2]

arr_np = np.array(arr)

idx = np.argmax(arr_np)

print(idx)