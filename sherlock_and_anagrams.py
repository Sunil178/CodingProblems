# Sherlock and Anagrams

string = "cdcd"
k = 0
anagrams = 0
while k < len(string)-1:
    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string)-k:
            str1 = string[i:i+(k+1)]
            str2 = string[j:j+(k+1)]
            c = 0
            for char in str1:
                if str1.count(char) == str2.count(char):
                    c += 1
            if c == len(str1):
                print(str1, ",", str2)
                anagrams += 1
            j += 1
        i += 1
    k += 1
print(anagrams)