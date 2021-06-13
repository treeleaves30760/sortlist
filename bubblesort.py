def bubblesort(L):
    num = len(L)
    for i in range(num):
        for j in range(num - i - 1):
            if (L[j] > L[j + 1]):
                L[j], L[j + 1] = L[j + 1], L[j]
    
    return L


L = [9,8,7,6,5,4,3,2,1]
print(bubblesort(L))
L.sort()
print(L)