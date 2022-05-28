from array import array
import math

arr = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]

def BinSearchRecursive(low: int, high: int, key: int) -> int:    
    if (low == high):
        if arr[low] == key:
            return low
        else:
            return -1
    else:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return BinSearchRecursive(mid+1, high, key)
        else:
            return BinSearchRecursive(low, mid-1, key)
l = 0
h = len(arr)-1
result = BinSearchRecursive(l, h, 12)
if result != -1:
    print(f"Element found at location {result+1}")
else:
    print("Element not in Array")
