# Array Manipulation

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
add = [3, 7, 1]
rg = [[1, 5], [4, 8], [6, 9]]
i = 0
while i < len(rg):
    j = rg[i][0] - 1
    while j < rg[i][1]:
        lst[j] += add[i]
        j += 1
    i += 1
print(max(lst))