# New Year Chaos

chaos = [2, 5, 1, 3, 4]
i = 0
bribe = 0
while i < len(chaos):
    diff = chaos[i] - (i+1)
    i += 1
    if diff > 2:
        print("Chaotic")
        break
    if diff > 0:
        bribe += diff
    if i == len(chaos):
        print("Not chaotic. Number of bribe is ", bribe)