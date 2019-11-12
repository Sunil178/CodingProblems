# Forgone Solution

t = int(input())
for test in range(1, t+1):
    no = int(input())
    if '4' in str(no):
        n = no
        i = 0
        while i < no:
            if ('4' not in str(i) and '4' not in str(n)) or ('4' not in str(n) and '4' not in str(i)):
                res = i + n
                if res == no:
                    print("Case #" + str(test) + ":", i, n)
                    break
            i += 1
            n -= 1