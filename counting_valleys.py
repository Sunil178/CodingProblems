# Counting Valleys

path = [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
number_of_path = 0
steps = 0
for nth_path in path:
    if nth_path == 0:
        steps -= 1
        state = 0
    else:
        steps += 1
        state = 1
    if steps > 0 and state == 1:
        number_of_path += 1
print(number_of_path)