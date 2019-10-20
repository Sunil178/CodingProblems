# Sorting: Bubble Sort


arr = [3, 2, 1]
i = 0
count = 0
while i < len(arr):
    j = 0
    while j < len(arr) - 1:
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            count += 1
        j += 1
    i += 1
print(count)