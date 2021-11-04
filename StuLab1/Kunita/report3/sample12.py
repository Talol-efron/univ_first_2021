import numpy as np;

def q(x,y):
    NaN = np.nan
    if (y==0):
        return NaN
    else:
        return x/y

print(q(3,1))
print(q(3,0))