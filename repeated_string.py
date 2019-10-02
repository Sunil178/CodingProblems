# Repeated String


string = "abcac"
limit = 10
new_string = ""
i = 0
while len(new_string) < limit:
    if i == len(string):
        i = 0
    new_string += string[i]
    i += 1
print(new_string.count('a'))