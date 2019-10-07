# Two Strings

limit = int(input())
str1 = []
str2 = []
for i in range(limit):
    str1.append(set(input()))
    str2.append(set(input()))
for i, j in zip(str1, str2):
    if i & j:
        print("YES")
    else:
        print("NO")