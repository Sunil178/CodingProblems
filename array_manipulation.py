# Array Manipulation

rg = list(map(int, input().split()))
lst= []
for i in range(rg[0]):
    lst.append(0)
add = []
for j in range(rg[1]):
    add.append(list(map(int, input().split())))
i = 0
while i < len(add):
    j = add[i][0] - 1
    while j < add[i][1]:
        lst[j] += add[i][2]
        j += 1
    i += 1
print(max(lst))
