# Alternating Characters

string = list("BBBBB")
i = 0
cnt = 0
while i < len(string) - 1:
    if string[i] == string[i + 1]:
        del string[i + 1]
        cnt += 1
        i -= 1
    i += 1
print(cnt)