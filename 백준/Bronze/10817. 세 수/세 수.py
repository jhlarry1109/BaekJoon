li = list(map(int,input().split()))
li.remove(max(li))
li.remove(min(li))
print(*li)