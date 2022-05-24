from array import array


def linearSearch(arr: array, n: int, x: int) -> int :
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


arr = [1,3,4,5,6]
x = 5
n = len(arr)
result = linearSearch(arr,n,x)
if result == -1:
    print("Elemenet not found")
else:
    print(f"Element found at index {result}")