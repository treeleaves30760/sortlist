def insertsort(L):
    re = []
    for i in L:
        for j in range(len(re)):
            if (i <= re[j]):
                re.insert(j, i)
                break
        else:
            re.append(i)
    return re

L = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
print(insertsort(L))
L.sort()
print(L)