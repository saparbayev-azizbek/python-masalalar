def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
def binsearch(arr, left, right, x):
    while(right - left > 1):
        middle = (right + left) // 2
        if arr[middle] > x:
            right = middle
        else:
            left = middle
    if (arr[left] == x):
        return left
    else:
        return -1
arr = [2,4,6,4,1,2]
arr = quicksort(arr)
print(arr)
print(binsearch(arr, 0, len(arr), 1))