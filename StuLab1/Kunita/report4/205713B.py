import numpy as np
import time


N = np.power(10,4)
A = np.random.rand(N, N)
B = np.random.rand(N, N)

print("A = {}".format(A))
print("B = {}".format(B))

X = np.zeros((N,N), np.float64)
t0 = time.time()
X = np.add(A, B)
t1 = time.time()
tx = t1 - t0
print("X = {}".format(X))
print("tx = {}".format(tx))

Y = np.zeros((N,N), np.float64)
t0 = time.time()
for i in range(N):
    for k in range(N):
        Y[i][k] = A[i][k] + B[i][k]
t1 = time.time()
ty = t1 - t0
print("Y = {}".format(Y))
print("ty = {}".format(ty))
