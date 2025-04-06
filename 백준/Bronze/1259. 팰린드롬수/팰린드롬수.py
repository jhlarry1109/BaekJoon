while 1:
    n = 0
    a = input()
    if a == "0":
        break
    li = []
    for i in range(len(a)//2):
        li.append(a[i])
    a = a[::-1]
    for i in range(len(a)//2):
        if li[i] != a[i]:
            print("no")
            n = 1
            break
    if n == 0:
        print("yes")