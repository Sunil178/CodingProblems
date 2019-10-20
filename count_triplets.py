# Count Triplets


nor = list(map(int, input().split()))
lst = list(map(int, input().split()))
r = nor[1]
i = 0
count = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[j] == lst[i] * r:
            k = j + 1
            while k < len(lst):
                if lst[k] == lst[j] * r:
                    print(lst[i], ", ", lst[j], ", ", lst[k])
                    count += 1
                k += 1
        j += 1
    i += 1
print(count)