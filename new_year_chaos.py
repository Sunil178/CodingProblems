# New Year Chaos

chaos = [2, 1, 5, 3, 4]
i = 0
chaotic = True
bribe = 0
while i < len(chaos):
    diff = chaos[i] - (i+1)
    if diff > 2:
        chaotic = True
        break
    else:
        chaotic = False
    if diff > 0:
        bribe += diff
    i += 1
if chaotic:
    print("Chaotic")
else:
    print("Not chaotic. Number of bribe is ", bribe)
