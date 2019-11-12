# Forgone Solution

tests = int(input())
for test in range(1, test+1):
    number = int(input())
    if '4' in str(number):
        last_number = number
        initial_number = 0
        while initial_number < number:
            if ('4' not in str(initial_number) and '4' not in str(last_number)) or ('4' not in str(last_number) and '4' not in str(initial_number)):
                result = initial_number + last_number
                if result == number:
                    print("Case #" + str(test) + ":", initial_number, last_number)
                    break
            initial_number += 1
            last_number -= 1