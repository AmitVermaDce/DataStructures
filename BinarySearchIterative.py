from array import array
import math
def BinSearch(arr: array, n: int, key: int) -> int:
    l = 0
    h = n-1    
    while (l<=h):   
        mid = (l + h)//2     
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            l = mid + 1 
        if key < arr[mid]:
            h = mid - 1
    return -1



arr = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
result = BinSearch(arr, len(arr), 61)
if result == -1:
    print("Element not found")
else:
    print(f'Element found at index {result}')
