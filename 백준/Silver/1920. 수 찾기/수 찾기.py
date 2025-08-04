n = int(input())
a = list(map(int,input().split()))
m = int(input())
li = list(map(int,input().split()))
a.sort()
for i in li:
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if a[mid] > i:
            right = mid-1
        elif a[mid] < i:
            left = mid+1
        else:
            break
    print(0 if left > right else 1)