def cal():
    num = ["000", "001", "010", "100", "101", "110", "111"]
    data1 = ""
    len_num = len(num)
    for i in range(len_num):
       data1 += num[i]
       i += 1
    return data1

print(cal())
