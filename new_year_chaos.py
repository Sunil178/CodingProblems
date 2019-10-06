# New Year Chaos

number = [1, 2, 3, 4, 5, 6, 7, 8]
chaos = [1, 2, 4, 5, 3, 8, 6, 7]
i = 0
chaotic = True
bribe = 0
while i < len(number):
    diff = i - chaos.index(number[i])
    if diff > 2:
        chaotic = True
    else:
        chaotic = False
    if diff > 0:
        bribe += diff
    i += 1
if chaotic:
    print("Chaotic")
else:
    print("Not chaotic. Number of bribe is ", bribe)