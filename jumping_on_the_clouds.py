# Jumping on the Clouds

clouds = [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
steps = 0
i = 0
while i < len(clouds) - 1:
    i += 2
    if i < len(clouds) - 1:
        if clouds[i] == 1:
            i -= 1
    steps += 1
print("steps: ", steps)