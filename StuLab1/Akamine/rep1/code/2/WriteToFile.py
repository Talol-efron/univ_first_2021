with open("out_python.txt", "w") as f:
    for i in range(1000*1000*10):
        f.write(str(i))