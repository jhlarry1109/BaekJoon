n = int(input())
for _ in range(n):
    a,b = input().split()
    for i in range(len(b)):
        if i == int(a)-1:
            continue
        print(b[i], end="")
    print()