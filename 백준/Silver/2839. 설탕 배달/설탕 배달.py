n = int(input())
a,b = -1,-1
sum = []
for i in range(0, n+1, 5):
    a += 1
    for j in range(0, n+1, 3):
        b += 1
        if i+j == n:
            sum.append(a+b)
    b = -1
if sum == []:
    print(-1)
else:
    print(min(sum))