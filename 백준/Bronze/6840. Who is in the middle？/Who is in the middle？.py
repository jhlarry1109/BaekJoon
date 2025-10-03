li = []
for i in range(3):
    li.append(int(input()))
li.remove(max(li))
li.remove(min(li))
print(*li)