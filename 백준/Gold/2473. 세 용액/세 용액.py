n = int(input())
li = list(map(int,input().split()))
li.sort()
min = abs(li[0] + li[1] + li[2])
ans = [li[0], li[1], li[2]]
for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        a = li[i] + li[left] + li[right]
        if abs(a) < min:
            min = abs(a)
            ans = [li[i], li[left], li[right]]
        if a < 0:
            left += 1
        else:
            right -= 1
print(*ans)