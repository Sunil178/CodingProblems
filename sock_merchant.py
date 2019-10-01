#Sock Merchant

def delete(socks, no):
    i = 0
    while i < len(socks):
        if socks[i] == no:
            socks.remove(socks[i])
            i -= 1
        i += 1
    return socks
socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
i = 0
number_of_socks = 0
while(i < len(socks)):
    if socks[0] in socks:
        counter = socks.count(socks[0])
        if counter % 2 != 0:
            counter -= 1
            number_of_socks += counter // 2
        else:
            number_of_socks += counter // 2
        socks = delete(socks, socks[0])
    i += 1
print(number_of_socks)