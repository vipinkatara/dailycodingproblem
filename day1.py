def selective_product(lis):
    pro = 1
    s = []
    for i in range(0, len(lis)):
        pro = 1
        for j in range(0, len(lis)):
            if(i != j):
                pro *= lis[j]
       #print(pro)
        s.append(pro)
    return s



lis = [1, 2, 3, 4, 5]
print(selective_product(lis))
