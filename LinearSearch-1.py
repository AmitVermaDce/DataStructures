from array import array
def getMissingNo(A: array) -> int:
    n = len(A)
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A)
    return int(total - sum_of_A)
 
 
# Driver program to test the above function
A = [1, 2, 3, 4, 6]
miss = getMissingNo(A)
print(miss)