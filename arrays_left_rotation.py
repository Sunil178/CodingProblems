# Arrays: Left Rotation

given_arr = [1, 2, 3, 4, 5]
temp_arr = []
left_rotate_number = 2
i = 0
while i < len(given_arr):
    if left_rotate_number == len(given_arr):
        left_rotate_number = 0
    temp_arr.append(given_arr[left_rotate_number])
    left_rotate_number += 1
    i += 1
print(temp_arr)