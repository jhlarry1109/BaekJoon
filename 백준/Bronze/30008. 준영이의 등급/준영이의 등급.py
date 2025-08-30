n, k = map(int,input().split())
li = list(map(int,input().split()))
for i in range(len(li)):
    li[i] = 100*li[i]//n
for i in li:
    if i <= 4:
        print(1, end=" ")
    elif i <= 11:
        print(2, end=" ")
    elif i <= 23:
        print(3, end=" ")
    elif i <= 40:
        print(4, end=" ")
    elif i <= 60:
        print(5, end=" ")
    elif i <= 77:
        print(6, end=" ")
    elif i <= 89:
        print(7, end=" ")
    elif i <= 96:
        print(8, end=" ")
    else:
        print(9, end=" ")