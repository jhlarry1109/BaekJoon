n = input()
star = n.index('*')
check = int(n[-1])

for i in range(10):
    total = 0
    for j in range(12):
        if j == star:
            digit = i
        else:
            digit = int(n[j])
        weight = 1 if j % 2 == 0 else 3
        total += digit * weight

    ans = (10 - total % 10) % 10
    if ans == check:
        print(i)
        break
