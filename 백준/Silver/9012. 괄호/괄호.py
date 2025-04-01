def ans(a):
    li = []
    top = -1
    for i in range(len(a)):
        if a[i] == '(':
            top += 1
            li.append(1)
        else:
            if top != -1:
                li.pop(top)
                top -= 1
            else:
                return "NO"
            
    if li:
        return "NO"
    else:
        return "YES"


t = int(input())
for i in range(t):
    a = input()
    print(ans(a))