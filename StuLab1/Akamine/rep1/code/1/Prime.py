x = 1
for i in range(3, 1000*50):
    dividable = False

    for j in range(2, i):
        if i % j == 0:
            dividable = True
            break

    if not dividable:
        x += 1

print("The number of primes =", x)
