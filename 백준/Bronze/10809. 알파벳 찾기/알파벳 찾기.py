a = input()
ans = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(len(a)):
    if ans[ord(a[i]) - 97] == -1:
        ans[ord(a[i]) - 97] = i
print(*ans)