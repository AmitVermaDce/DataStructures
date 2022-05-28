from array import array
from cgitb import reset
from unittest import result

arr = [9, 3, 7, 5, 6, 4, 8, 2]

def MergeSortRecursive(arr) -> array:
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSortRecursive(L)
        MergeSortRecursive(R)

        i = 0; j = 0; k = 0
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while(i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1
        while(j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


result = MergeSortRecursive(arr)
print(result)
