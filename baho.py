n = int(input())
s = 0
if n >= 38:
    for i in range(3):
        if (n + i) % 5 == 0:
            s = n + i
            break
        else:
            s = n
    print(s)
else:
    print(n)