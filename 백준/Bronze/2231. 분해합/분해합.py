n = int(input())
sum = 0
for i in range(1, n+1):
    for j in range(0, len(str(i))):
        sum += int(str(i)[j])
    if i + sum == n:
        print(i)
        exit()
    sum = 0
print(0)