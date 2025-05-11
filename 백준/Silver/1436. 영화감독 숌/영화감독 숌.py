n = int(input())
i = 0
num  = 0
while 1:
    i += 1
    ans = str(i)
    if '666' in ans:
        num += 1
        if num == n:
            break
print(ans)