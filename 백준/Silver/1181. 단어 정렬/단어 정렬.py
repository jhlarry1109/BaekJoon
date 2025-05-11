n = int(input())
li = []
for i in range(n):
    li.append(input())
li = set(li)
li = list(li)
while 1:
    c = 0
    for i in range(len(li)-1):
        if len(li[i]) > len(li[i+1]):
            li[i], li[i+1] = li[i+1], li[i]
            c = 1
    if c == 0:
        break
while 1:
    c = 0
    for i in range(len(li)-1):
        if li[i] > li[i+1] and len(li[i]) == len(li[i+1]):
            li[i], li[i+1] = li[i+1], li[i]
            c = 1
    if c == 0:
        break
for i in range(len(li)):
    print(li[i])