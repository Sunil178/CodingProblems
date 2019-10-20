# Frequency Queries


data = []
limit = int(input())
i = 0
while i < limit:
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        data.append(lst[1])
    if lst[0] == 2:
        if lst[1] in data:
            data.remove(lst[1])
    if lst[0] == 3:
        no = [element for element in data if data.count(element) == lst[1]]
        if no == []:
            print('0')
        else:
            print('1')
    i += 1