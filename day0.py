def fin_pair_sum(lis, k):

    if(len(lis) > 0):
        for i in range(0, len(lis)):
            num = k - lis[i]
            if num in lis:
                return True
        return False
    else:
        return False

print('Enter list')
s = input()
lis = list(map(int, s.split()))
print('Enter k......')
k = int(input())
#k = int(input())
print(fin_pair_sum(lis, k))

