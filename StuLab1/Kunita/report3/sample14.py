import numpy as np
import math

NaN = np.nan
def r(x):
    if (x%math.pi/2==0):
        return NaN
    else:
        return np.arcsin(x)

print(r(1)) # pi/2
print(r(-1)) # -pi/2
print(r(0))