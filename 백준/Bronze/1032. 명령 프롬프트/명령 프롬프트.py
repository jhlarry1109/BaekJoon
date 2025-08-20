n = int(input())
li = []
ans = []
for i in range(n):
    li.append(input())

for i in range(len(li[0])):
    a = li[0][i]
    same = True
    for j in range(1,n):
        if a != li[j][i]:
            same = False
            break
    if same:
        ans.append(a)
    else:
        ans.append('?')
print(*ans, sep="")