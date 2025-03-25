n = int(input())
for i in range(n):
    ans = 0
    score = 1
    a = input()
    for j in range(len(a)):
        if a[j] == 'O':
            ans += score
            score += 1
        else:
            score = 1
    print(ans)