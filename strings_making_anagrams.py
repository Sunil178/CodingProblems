#	Strings: Making Anagrams

string1 = list(input())
string2 = list(input())
i = 0
while i < len(string1):
    letter = string1[i]
    index = string1.index(string1[i])
    if letter in string2:
        string1.remove(letter)
        string2.remove(letter)
        if i == index:
            i -= 1
    i += 1
print(len(string1) + len(string2))