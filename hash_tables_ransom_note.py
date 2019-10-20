# Hash Tables: Ransom Note


magazine = input().split()
note = input().split()
i = 0
c = 0
while i < len(note):
    if note[i] not in magazine:
        print("No")
        break
    else:
        magazine.remove(note[i])
    i += 1
if i == len(note):
    print("Yes")