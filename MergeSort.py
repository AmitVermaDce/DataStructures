from array import array

def MergeSort(A: array, B: array) -> array:
    i,j = 0, 0; C = []
    while(i<len(A) and j<len(B)):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1            
        else:
            C.append(B[j])
            j += 1
        
    while (i<len(A)):
        C.append(A[i])
        i += 1
    while (j<len(B)):
        C.append(B[j])
        j += 1
    return C
         

A = [2, 8, 15, 18]
B = [5, 9, 12, 17, 21, 34, 45]
result = MergeSort(A, B)
print(result)