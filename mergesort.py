def merge(L, B):
    re = []
    indL = 0
    indR = 0
    limL = len(L)
    limR = len(B)
    while indL < limL or indR < limR:
        if indL == limL:
            re.extend(B[indR:])
            break
        elif indR == limR:
            re.extend(L[indL:])
            break
        elif (L[indL] <= B[indR]):
            re.append(L[indL])
            indL += 1
        elif (L[indL] > B[indR]):
            re.append(B[indR])
            indR += 1

    return re

def mergesort(L):
    if (len(L) <= 1):
        return L
    num = len(L) // 2
    return merge(mergesort(L[:num]), mergesort(L[num:]))

l = [9,8,7,6,5,4,1,3,5,4,6,2,2,8,4,1,3,2,1,0]
print(mergesort(l))
l.sort()
print(l)