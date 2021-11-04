import numpy as np

np.seterr(divide='ignore', invalid='ignore')
arr = [1, np.e, np.e**2, 0]
def s(x):
    if (x==0):
        return np.log(x)
    else:
        return np.log(x)

print(s(arr))

