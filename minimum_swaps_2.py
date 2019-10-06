# Minimum Swaps 2

arr = [7, 1, 3, 2, 4, 5, 6]
i = 0
count = 0
while i < len(arr) - 1:
    ind = arr.index(min(arr[(i+1):len(arr)]))
    if arr[i] > arr[ind]:
        arr[i], arr[ind] = arr[ind], arr[i]
        count += 1
    i += 1
print(count)