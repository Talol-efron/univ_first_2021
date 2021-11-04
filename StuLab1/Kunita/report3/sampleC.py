import numpy as np
import math

NaN = np.nan

def calc(x): #円の面積を求める関数
    if(x==0): # x=0の時は面積が出ないので、nanを返す
        return NaN
    else:
        return x*x*math.pi

print(calc(1))
print(calc(2))
print(calc(0))
