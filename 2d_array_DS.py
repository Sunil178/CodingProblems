# 2D Array - DS


arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
i = 0
total = 0
hourglass = []
while i < len(arr) - 2:
    j = 0
    while j < len(arr) - 2:
        total += arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        hourglass.append(total)
        total = 0
        j += 1
    i += 1
print(max(hourglass))