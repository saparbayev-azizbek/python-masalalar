def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
matn = input()
arr = []
son = ''
matn += ':'
for i in range(0,len(matn)):
    if matn[i] != ':':
        son += matn[i]
    else:
        arr.append(int(son))
        son = ''
arr = quicksort(arr)
for i in arr:
    print(i, end=" ")